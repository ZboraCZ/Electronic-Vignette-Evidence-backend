# -*- coding: utf-8 -*-

from django.utils import timezone
from drf_spectacular.utils import extend_schema
from eve.users.operations import get_one_user
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .operations import (
    get_active_vignette_by_license_plate,
    get_all_vignette_types,
    get_all_vignettes_by_license_plate,
    get_one_vignette_by_id,
    get_one_vignette_type,
    get_validated_vignette_by_license_plate, get_actual_and_future_vignettes,
)
from .serializers import (
    BuyVignetteSerializer,
    DelayVignetteSerializer,
    ExtendVignetteSerializer,
    QuickBuyVignetteSerializer,
    ValidatedVignetteSerializer,
    VignetteSerializer,
    VignetteTypeSerializer,
)
from .services import (
    create_new_vignette,
    create_new_vignette_quick,
    delay_vignette,
    extend_vignette,
)


class VignetteTypesView(APIView):
    permission_classes = []

    @staticmethod
    @extend_schema(responses={200: VignetteTypeSerializer(many=True)})
    def get(request):
        types = get_all_vignette_types()
        serializer = VignetteTypeSerializer(types, many=True)
        return Response(serializer.data)

    @staticmethod
    @extend_schema(
        request=VignetteTypeSerializer, responses={200: VignetteTypeSerializer}
    )
    def patch(request, vignette_type_id):
        data = request.data
        vignette_type = get_one_vignette_type(vignette_type_id)
        serializer = VignetteTypeSerializer(data=data)

        if serializer.is_valid():
            serializer.update(vignette_type, serializer.validated_data)
            updated_vignette_types = get_one_vignette_type(vignette_type_id)
            vignette_type_serializer = VignetteTypeSerializer(updated_vignette_types)
            return Response(vignette_type_serializer.data)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class ActiveVignetteView(APIView):
    @staticmethod
    @extend_schema(responses={200: VignetteSerializer(many=True)})
    def get(request, license_plate):
        active_vignettes = get_actual_and_future_vignettes(license_plate)
        serializer = VignetteSerializer(active_vignettes, many=True)
        return Response(serializer.data)


class LicensePlateValidateView(APIView):
    authentication_classes = []
    permission_classes = []

    @staticmethod
    @extend_schema(responses={200: ValidatedVignetteSerializer})
    def get(request, license_plate):
        valid = get_validated_vignette_by_license_plate(license_plate)
        serializer = ValidatedVignetteSerializer(valid)
        return Response(serializer.data, status=status.HTTP_200_OK)


class QuickBuyView(APIView):
    authentication_classes = []
    permission_classes = []

    @staticmethod
    @extend_schema(
        request=QuickBuyVignetteSerializer, responses={200: QuickBuyVignetteSerializer}
    )
    def post(request, license_plate):
        data = request.data
        serializer_quick_buy = QuickBuyVignetteSerializer(data=data)
        serializer_quick_buy.is_valid(raise_exception=True)
        vignette_type = get_one_vignette_type(
            serializer_quick_buy.validated_data["id_vignette_type"]
        )
        valid_from = serializer_quick_buy.validated_data["valid_from"]
        create_new_vignette_quick(vignette_type, valid_from, license_plate)
        return Response(
            serializer_quick_buy.validated_data, status=status.HTTP_201_CREATED
        )


class BuyView(APIView):
    @staticmethod
    @extend_schema(
        request=BuyVignetteSerializer, responses={200: BuyVignetteSerializer}
    )
    def post(request, license_plate):
        data = request.data
        serializer_buy = BuyVignetteSerializer(data=data)
        serializer_buy.is_valid(raise_exception=True)
        vignette_type = get_one_vignette_type(
            serializer_buy.validated_data["id_vignette_type"]
        )
        valid_from = serializer_buy.validated_data["valid_from"]
        user = get_one_user(serializer_buy.validated_data["id_user"])
        create_new_vignette(user, vignette_type, valid_from, license_plate)
        return Response(serializer_buy.data, status=status.HTTP_201_CREATED)


class ExtendView(APIView):
    @staticmethod
    @extend_schema(
        request=ExtendVignetteSerializer, responses={200: ExtendVignetteSerializer}
    )
    def post(request, vignette_id):
        data = request.data
        serializer = ExtendVignetteSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        extend_vignette(
            get_one_vignette_by_id(vignette_id),
            get_one_vignette_type(serializer.data["vignette_type_id"]),
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DelayView(APIView):
    @staticmethod
    @extend_schema(
        request=DelayVignetteSerializer, responses={200: DelayVignetteSerializer}
    )
    def post(request, vignette_id):
        data = request.data
        serializer = DelayVignetteSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        delay_vignette(
            get_one_vignette_by_id(vignette_id), serializer.data["delay_date"]
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RemoveView(APIView):
    @staticmethod
    @extend_schema(responses={200: None})
    def delete(request, vignette_id):
        get_one_vignette_by_id(vignette_id).delete()
        return Response(status=status.HTTP_200_OK)


class HistoryView(APIView):
    @staticmethod
    @extend_schema(responses={200: VignetteSerializer(many=True)})
    def get(request, license_plate):
        serializer = VignetteSerializer(
            get_all_vignettes_by_license_plate(license_plate), many=True
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class VignetteEditView(APIView):
    @staticmethod
    @extend_schema(
        request=VignetteSerializer,
        responses={200: VignetteSerializer}
    )
    def patch(request, vignette_id):
        data = request.data
        vignette = get_one_vignette_by_id(vignette_id)
        serializer = VignetteSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            vignette_type_id = request.data["vignette_type_id"]
            vignette.vignette_type = get_one_vignette_type(vignette_type_id)
            serializer.update(vignette, serializer.validated_data)
            return Response(VignetteSerializer(vignette).data)

        return Response(status=status.HTTP_400_BAD_REQUEST)
