
from rest_framework import generics, filters, status, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product
from products.serializers import ProductSerializer
from shops.models import Shop
from shops.serializers import ShopSerializer, ShopDetailSerializer


class ShopListCreateApiView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ('name',)


class ShopDetailAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_shop(self, num):
        shop = get_object_or_404(Shop, pk=num)
        return shop

    def get(self, request, num):
        shop = self.get_shop(num)

        s_serializer = ShopDetailSerializer(shop)

        return Response(s_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, num):
        shop = self.get_shop(num)
        serializer = ShopSerializer(shop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, num):
        shop = self.get_shop(num)
        shop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
