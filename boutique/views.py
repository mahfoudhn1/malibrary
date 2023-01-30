from django.http import Http404

# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from boutique.models import Boutique
from boutique.serializer import BoutiqueSerializer


class BoutiqueAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Boutique.objects.get(pk=pk)
        except Boutique.DoesNotExist:
            raise Http404

    def post(self, request):
        serializer = BoutiqueSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(owner=request.user)

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request):
    #     clients = User.objects.all()
    #     serialzer = ClientSerializer(data=clients)
    #     content = {
    #         'clients': 'serialzer.data'
    #     }
    #     return Response(content)

    def patch(self, request, pk):

        boutique = self.get_object(pk=pk)

        serializer = BoutiqueSerializer(boutique, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        client = self.get_object(pk=pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
