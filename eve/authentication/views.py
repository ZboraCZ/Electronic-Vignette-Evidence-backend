# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from eve.authentication.serializers import AuthUsersSerializer, TokenSerializer
from eve.users.models import Users


class RegistrationView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serializer = AuthUsersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serializer = AuthUsersSerializer(data=data)
        if serializer.is_valid():
            user = Users.objects.get(email=request.data["email"])
            token = Token.objects.get(user=user)
            s2 = TokenSerializer(token)
            return Response(s2.data)
        return Response("OK")
