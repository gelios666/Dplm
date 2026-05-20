from rest_framework.views import APIView
from rest_framework.response import Response


class TestUserView(APIView):

    def get(self, request):
        return Response({'message': 'Users API works'})