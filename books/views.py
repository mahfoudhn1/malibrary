from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.views import APIView

from boutique.models import Boutique
from boutique.serializer import BoutiqueSerializer
from .models import Book, Category
from .serializers import BookSerializer
from rest_framework.parsers import MultiPartParser, FormParser



class BookAPI(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def get_object(pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, *args, **kwargs):
        books = Book.objects.all()

        serializer = BookSerializer(data=books, many=True)

        if serializer.is_valid():
            print(serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def post(self, request):

        data = request.data

        serializer = BookSerializer(data=data)
        boutique = Boutique.objects.get(owner=request.user)
        if serializer.is_valid():
            serializer.save(seller=request.user, boutique=boutique)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):

        book = self.get_object(pk=pk)
        parser_classes = (MultiPartParser, FormParser)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_object(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
