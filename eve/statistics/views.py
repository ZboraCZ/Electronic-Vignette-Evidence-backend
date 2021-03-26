# -*- coding: utf-8 -*-

from rest_framework.response import Response
from rest_framework.views import APIView

from .operations import get_statistics
from .serializers import StatisticsSerializer


class StatisticsView(APIView):
    @staticmethod
    def get(request):
        latest_statistics = get_statistics()
        serializer = StatisticsSerializer(latest_statistics)
        return Response(serializer.data)
