from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

from .operations import get_one_user, get_users_license_plate
from .serializers import UsersSerializer, LicensePlateSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class UsersLicensePlateView(APIView):
    @staticmethod
    def get(request, user_id):
        license_plate = get_users_license_plate(user_id)
        serializer = LicensePlateSerializer(data=license_plate, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UsersView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    @extend_schema(
        responses={200: UsersSerializer}
    )
    def get(request, user_id):
        user = get_one_user(user_id)
        serializer = UsersSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    @extend_schema(
        request=UsersSerializer,
        responses={200: UsersSerializer}
    )
    def patch(request, user_id):
        data = request.data
        user = get_one_user(user_id)
        serializer = UsersSerializer(data=data)

        if serializer.is_valid():
            serializer.update(user, serializer.validated_data)
            return Response(serializer.data)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
