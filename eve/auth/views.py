# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class RegistrationView(APIView):
    @staticmethod
    def post(request):
        return Response("OK")


class LoginView(APIView):
    @staticmethod
    def post(request, license_plate):
        return Response("OK")


class LogoutView(APIView):
    @staticmethod
    def get(request):
        return Response("OK")
