# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .operations import get_all_vignette_types, get_one_vignette_type
from .serializers import VignetteTypeSerializer
from .models import VignetteType


class VignetteTypesView(APIView):
    @staticmethod
    def get(request):
        types = get_all_vignette_types()
        serializer = VignetteTypeSerializer(types, many=True)
        return Response(serializer.data)

    @staticmethod
    def patch(request, vignette_type_id):
        data = request.data
        vignette_type = get_one_vignette_type(vignette_type_id)
        serializer = VignetteTypeSerializer(data=data)

        if serializer.is_valid():
            serializer.update(vignette_type, serializer.validated_data)
            return Response(serializer.data)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)