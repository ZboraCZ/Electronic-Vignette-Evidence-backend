from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .operations import get_one_user
from .serializers import UsersSerializer


class UsersView(APIView):
    @staticmethod
    def get(request, user_id):
        user = get_one_user(user_id)
        serializer = UsersSerializer(user, many=False)
        return Response(serializer.data)

    @staticmethod
    def patch(request, user_id):
        data = request.data
        user = get_one_user(user_id)
        serializer = UsersSerializer(data=data)

        if serializer.is_valid():
            serializer.update(user, serializer.validated_data)
            return Response(serializer.data)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
