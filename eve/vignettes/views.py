# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .operations import get_all_vignette_types, get_one_vignette_type, get_active_vignette_by_license_plate
from .serializers import VignetteTypeSerializer, VignetteSerializer


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


class VignettesView(APIView):
    @staticmethod
    def get(request, license_plate):
        active_vignette = get_active_vignette_by_license_plate(license_plate)
        serializer = VignetteSerializer(active_vignette)
        return Response(serializer.data)
