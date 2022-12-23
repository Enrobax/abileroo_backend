from rest_framework import generics, status, permissions
from django_filters import rest_framework as searchfilters
from django.db import transaction
from rest_framework.response import Response
from rest_framework.views import APIView

from orders.filters import OrderFilter
from orders.models import Order
from orders.serializers import OrderSerializer, OrderDetailSerializer
from products.models import Product


class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (searchfilters.DjangoFilterBackend,)
    filterset_class = OrderFilter


class OrderCreateAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request):
        try:
            new_order_serializer = OrderSerializer(data=request.data)
            order_detail_data = request.data["details"]

        except:
            return Response({"Error": "Invalid request body"})

        if new_order_serializer.is_valid() and len(order_detail_data) > 0:
            try:
                with transaction.atomic():
                    order = new_order_serializer.save()
                    correct_order_detail_list = []
                    for order_detail in order_detail_data:
                        rdict = {
                            "amount": order_detail["amount"],
                            "order": order.id,
                            "product": order_detail["product"]
                        }
                        correct_order_detail_list.append(rdict)

                    order_detail_serializer = OrderDetailSerializer(data=correct_order_detail_list, many=True)

                    if order_detail_serializer.is_valid():

                        order_detail_serializer.save()

                        # aggiorno quantità prodotto disponibile

                        for correct_order_detail in correct_order_detail_list:
                            product = Product.objects.get(id=correct_order_detail["product"])
                            product.available_amount = product.available_amount - correct_order_detail["amount"]
                            product.save()

                        return Response(new_order_serializer.data, status=status.HTTP_201_CREATED)

            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        elif new_order_serializer.errors:
            return Response({"Error": new_order_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Message": "Empty order detail list"}, status=status.HTTP_400_BAD_REQUEST)
