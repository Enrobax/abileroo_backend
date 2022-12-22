from django.urls import path

from orders.views import OrderListAPIView, OrderCreateAPIView

urlpatterns = [
    path('orders/', OrderListAPIView.as_view(), name="order-list"),
    path('order-create/', OrderCreateAPIView.as_view(), name="order-create")
]
