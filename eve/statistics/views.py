# -*- coding: utf-8 -*-

from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

from .operations import get_statistics
from .serializers import StatisticsSerializer


class StatisticsView(APIView):
    @staticmethod
    @extend_schema(
        responses={200: StatisticsSerializer}
    )
    def get(request):
        latest_statistics = get_statistics()
        serializer = StatisticsSerializer(latest_statistics)
        return Response(serializer.data)
