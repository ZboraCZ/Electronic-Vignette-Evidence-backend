# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

from eve.authentication.operations import generate_token_response, encrypt_password_in_dict, generate_email_response, \
    generate_password_response
from eve.authentication.serializers import AuthUsersSerializer, TokenSerializer, AuthErrorSerializer
from eve.exceptions import DataValidationFailed
from eve.users.models import Users
from eve.users.serializers import UsersAuthSerializer
from eve.utils import encrypt_string


class RegistrationView(APIView):
    permission_classes = []

    @staticmethod
    @extend_schema(
        request=UsersAuthSerializer,
        responses={200: TokenSerializer}
    )
    def post(request):
        data = request.data
        encrypt_password_in_dict(data)
        serializer = UsersAuthSerializer(data=data)

        if serializer.is_valid():
            user = serializer.save()
            response = generate_token_response(user)
            token_serializer = TokenSerializer(response)
            return Response(token_serializer.data, status=status.HTTP_200_OK)
        raise DataValidationFailed()


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
        if serializer.is_valid():
            try:
                user = Users.objects.get(email=request.data["email"])
            except Users.DoesNotExist:
                email_response = generate_email_response()
                email_response_serializer = AuthErrorSerializer(email_response)
                return Response(email_response_serializer.data, status=status.HTTP_401_UNAUTHORIZED)

            if encrypt_string(request.data["password"]) == user.password:
                token_response = generate_token_response(user)
                token_response_serializer = TokenSerializer(token_response)
                return Response(token_response_serializer.data, status=status.HTTP_200_OK)
            else:
                password_response = generate_password_response()
                password_response_serializer = AuthErrorSerializer(password_response)
                return Response(password_response_serializer.data, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

