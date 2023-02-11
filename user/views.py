from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework import status

class UserView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        if request.user.is_anonymous:
            return Response({
                'message': 'User is not logged in'
            }, status=status.HTTP_401_UNAUTHORIZED)
        user_serializer = UserSerializer(request.user)
        return Response(user_serializer.data)

    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = User(username=user_serializer.data['username'], email=user_serializer.data['email'])
            user.set_password(user_serializer.data['password'])
            user.save()
            return Response(UserSerializer(user).data)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        if request.user.is_anonymous:
            return Response({
                'message': 'User is not logged in'
            }, status=status.HTTP_401_UNAUTHORIZED)
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        if request.user.is_anonymous:
            return Response({
                'message': 'User is not logged in'
            }, status=status.HTTP_401_UNAUTHORIZED)
        request.user.delete()
        return Response({
            'message': 'User deleted'
        })
