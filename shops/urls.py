from django.urls import path

from shops.views import ShopListCreateApiView, ShopDetailAPIView

urlpatterns = [
    path('shops/', ShopListCreateApiView.as_view(), name="shop-list"),
    path('shop/<int:num>/', ShopDetailAPIView.as_view(), name="shop-detail")
]
