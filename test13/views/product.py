from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from test13.models import *
from test13.serializers import ProductsSerializer


class ProductsViewSet(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(Product.objects.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

