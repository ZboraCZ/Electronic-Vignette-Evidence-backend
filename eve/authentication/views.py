# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from drf_spectacular.utils import extend_schema

from eve.authentication.serializers import AuthUsersSerializer, TokenSerializer, AuthErrorSerializer
from eve.users.models import Users
from eve.users.serializers import UsersAuthSerializer, UsersSerializer
from eve.utils import encrypt_string


class RegistrationView(APIView):
    permission_classes = []

    @staticmethod
    @extend_schema(
        request=UsersSerializer,
        responses={200: TokenSerializer}
    )
    def post(request):
        data = request.data
        password_hash = encrypt_string(data["password"])
        data["password"] = password_hash
        serializer = UsersAuthSerializer(data=data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user).key
            data["accessToken"] = token
            data["userId"] = user.id
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = []

    @staticmethod
    @extend_schema(
        request=AuthUsersSerializer,
        responses={
            200: TokenSerializer,
            401: AuthErrorSerializer
        }
    )
    def post(request):
        data = request.data
        serializer = AuthUsersSerializer(data=data)
        data = {}
        if serializer.is_valid():
            try:
                user = Users.objects.get(email=request.data["email"])
            except:
                data["error"] = "AUTH_ERROR"
                data["message"] = "wrong email"
                return Response(data, status=status.HTTP_401_UNAUTHORIZED)
            if encrypt_string(request.data["password"]) == user.password:
                token = Token.objects.get(user=user).key
                data["accessToken"] = token
                data["userId"] = user.id
                return Response(data, status=status.HTTP_200_OK)
            else:
                data["error"] = "AUTH_ERROR"
                data["message"] = "wrong password"
                return Response(data, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
