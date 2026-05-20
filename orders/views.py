from rest_framework.views import APIView
from rest_framework.response import Response


class TestOrdersView(APIView):

    def get(self, request):
        return Response({'message': 'Orders API works'})