from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.permissions import AllowAny

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView


from clients.models import Client
from clients.serializers import RegisterSerializer, LoginSerializer, ClientSerializer

class ClientsAPI(APIView):

    def get_object(self, pk):
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise Http404

    def post(self, request):
        data = request.data
        serializer = ClientSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        client = Client.objects.get(user=request.user)
        print(client)
        serializer = ClientSerializer(client)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):

        client = self.get_object(pk=pk)

        serializer = ClientSerializer(client, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        client = self.get_object(pk=pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class RegisterAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                "status": False,
                "message": serializer.errors

            }, status.HTTP_400_BAD_REQUEST)
        serializer.save()

        return Response({"status": True, "message": "user created"}, status.HTTP_200_OK)


class LoginAPI(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):

        print("excuted")
        data = request.data
        
        print(data)
        
        serializer = LoginSerializer(data=data)
        if not serializer.is_valid():
            print(serializer.errors)

            return Response({
                "status": False,
                "message": serializer.errors

            }, status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=serializer.data["username"],
                            password=serializer.data["password"])
        if not user:
            return Response({
                "status": False,
                "message": 'invalid criditionals'

            }, status.HTTP_400_BAD_REQUEST)
        token = Token.objects.get_or_create(user=user)
        return Response({"status": True, "message": "logedin", "token": str(token)}, status.HTTP_201_CREATED)

