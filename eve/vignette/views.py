# -*- coding: utf-8 -*-

from rest_framework.response import Response
from rest_framework.views import APIView

from .operations import get_all_vignette_types
from .serializers import VignetteTypeSerializer


class VignetteTypesView(APIView):
    @staticmethod
    def get(request):
        types = get_all_vignette_types()
        serializer = VignetteTypeSerializer(types, many=True)
        return Response(serializer.data)
