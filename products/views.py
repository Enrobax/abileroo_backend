from rest_framework import status, generics, filters, permissions
from django_filters import rest_framework as searchfilters
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from abileroo.permissions import IsAdminUserOrReadOnly
from products.filters import ProductFilter
from products.models import Product
from products.serializers import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (searchfilters.DjangoFilterBackend, filters.OrderingFilter,)
    filterset_class = ProductFilter
    ordering_fields = ['name']


class ProductDetailAPIView(APIView):
    permission_classes = (IsAdminUserOrReadOnly,)

    def get_product(self, id):
        product = get_object_or_404(Product, pk=id)
        return product

    def get(self, request, id):
        product = self.get_product(id)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        product = self.get_product(id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        product = self.get_product(id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
