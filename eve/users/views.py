from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

from .operations import get_one_user, get_user_by_email, get_users_licence_plates, get_users_history
from .serializers import UsersSerializer, LicensePlateSerializer, EditUserSerializer

from eve.vignettes.serializers import VignetteSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ..authentication.operations import check_user
from ..exceptions import DataValidationFailed


class UsersLicensePlateView(APIView):
    @staticmethod
    @extend_schema(
        responses={200: LicensePlateSerializer(many=True)}
    )
    def get(request, user_id):
        check_user(request, user_id)
        license_plate = get_users_licence_plates(user_id)
        serializer = LicensePlateSerializer(license_plate, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UsersVignetteHistoryView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    @extend_schema(
        responses={200: VignetteSerializer(many=True)}
    )
    def get(request, user_id):
        check_user(request, user_id)
        user_history = get_users_history(user_id)
        serializer = VignetteSerializer(user_history, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UsersDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    @extend_schema(
        responses={200: UsersSerializer}
    )
    def get(request, user_id):
        check_user(request, user_id)
        user = get_one_user(user_id)
        serializer = UsersSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    @extend_schema(
        request=UsersSerializer,
        responses={200: UsersSerializer}
    )
    def patch(request, user_id):
        check_user(request, user_id)
        data = request.data
        user = get_one_user(user_id)
        serializer = EditUserSerializer(data=data)

        if serializer.is_valid():
            serializer.update(user, serializer.validated_data)
            updated_user = get_one_user(user_id)
            updated_serializer = UsersSerializer(updated_user)
            return Response(updated_serializer.data)
        raise DataValidationFailed()


class UsersLookupView(APIView):
    @staticmethod
    @extend_schema(
        responses={200: UsersSerializer}
    )
    def get(request, user_email):
        check_user(request, None)
        user = get_user_by_email(user_email)
        serializer = UsersSerializer(user)
        return Response(serializer.data)
