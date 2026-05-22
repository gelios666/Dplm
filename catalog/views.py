from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated,
)

from users.permissions import IsShop

from .filters import ProductFilter
from .models import (
    Category,
    Product,
)
from .serializers import (
    CategorySerializer,
    ProductSerializer,
)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()

    serializer_class = CategorySerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(
        is_active=True
    )

    serializer_class = ProductSerializer

    filter_backends = [
        DjangoFilterBackend,
    ]

    filterset_class = ProductFilter


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    permission_classes = [
        IsAuthenticated,
        IsShop,
    ]


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()

    serializer_class = ProductSerializer


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()

    serializer_class = ProductSerializer

    permission_classes = [
        IsAuthenticated,
        IsShop,
    ]

    def perform_update(self, serializer):
        serializer.save(
            shop=self.request.user
        )


class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()

    permission_classes = [
        IsAuthenticated,
        IsShop,
    ]