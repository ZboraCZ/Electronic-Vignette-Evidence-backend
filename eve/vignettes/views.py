# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .operations import get_all_vignette_types, get_one_vignette_type, get_active_vignette_by_license_plate, \
    get_one_vignette_by_id, get_validated_vignette_by_license_plate,  \
    get_all_vignettes_by_licence_plate
from eve.users.operations import get_one_user
from .serializers import VignetteTypeSerializer, VignetteSerializer, ValidatedVignetteSerializer, \
    BuyVignetteSerializer, ExtendVignetteSerializer, DelayVignetteSerializer, QuickBuyVignetteSerializer

from .services import create_new_vignette, create_new_vignette_quick, extend_vignette, delay_vignette

from django.utils import timezone


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
            vignette_types = get_all_vignette_types()
            vignette_type_serializer = VignetteTypeSerializer(vignette_types, many=True)
            return Response(vignette_type_serializer.data)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class ActiveVignetteView(APIView):
    @staticmethod
    def get(request, license_plate):
        active_vignettes = get_active_vignette_by_license_plate(license_plate)
        serializer = VignetteSerializer(active_vignettes, many=True)
        return Response(serializer.data)


class LicensePlateValidateView(APIView):
    @staticmethod
    def get(request, license_plate):
        validated_vignette = get_validated_vignette_by_license_plate(license_plate)
        serializer = ValidatedVignetteSerializer(validated_vignette)
        return Response(serializer.data)


class QuickBuyView(APIView):
    @staticmethod
    def post(request, license_plate):
        data = request.data
        serializer_quick_buy = QuickBuyVignetteSerializer(data=data)
        serializer_quick_buy.is_valid(raise_exception=True)
        vignette_type = get_one_vignette_type(serializer_quick_buy.validated_data["id_vignette_type"])
        valid_from = serializer_quick_buy.validated_data["valid_from"]
        create_new_vignette_quick(vignette_type, valid_from, license_plate)
        return Response(serializer_quick_buy.validated_data, status=status.HTTP_201_CREATED)


class BuyView(APIView):
    @staticmethod
    def post(request, license_plate):
        data = request.data
        serializer_buy = BuyVignetteSerializer(data=data)
        serializer_buy.is_valid(raise_exception=True)
        vignette_type = get_one_vignette_type(serializer_buy.validated_data["id_vignette_type"])
        valid_from = serializer_buy.validated_data["valid_from"]
        user = get_one_user(serializer_buy.validated_data["id_user"])
        create_new_vignette(user, vignette_type, valid_from, license_plate)
        return Response(serializer_buy.data, status=status.HTTP_201_CREATED)


class ExtendView(APIView):
    @staticmethod
    def post(request, vignette_id):
        data = request.data
        serializer = ExtendVignetteSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        extend_vignette(get_one_vignette_by_id(vignette_id), get_one_vignette_type(serializer.data["vignette_type_id"]),
                        timezone.now())
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DelayView(APIView):
    @staticmethod
    def post(request, vignette_id):
        data = request.data
        serializer = DelayVignetteSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        delay_vignette(get_one_vignette_by_id(vignette_id), serializer.data["delay_date"])
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RemoveView(APIView):
    @staticmethod
    def delete(request, vignette_id):
        get_one_vignette_by_id(vignette_id).delete()
        return Response(status=status.HTTP_201_CREATED)


class HistoryView(APIView):
    @staticmethod
    def get(request, license_plate):
        serializer = VignetteSerializer(get_all_vignettes_by_licence_plate(license_plate))
        return Response(serializer.data)