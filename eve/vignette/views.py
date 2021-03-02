# -*- coding: utf-8 -*-

from rest_framework.response import Response
from rest_framework.views import APIView


class VignetteDetailsView(APIView):
    @staticmethod
    def get(request):
        return Response("OK")
