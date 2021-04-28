# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

from .operations import get_all_roles
from .serializers import RoleSerializer


class RolesView(APIView):
    @staticmethod
    @extend_schema(
        responses={200: RoleSerializer}
    )
    def get(request):
        all_roles = get_all_roles()
        serializer = RoleSerializer(all_roles, many=True)
        return Response(serializer.data)
