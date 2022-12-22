from django.urls import path

from products.views import ProductListCreateAPIView, ProductDetailAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name="product-list"),
    path('product/<int:id>/', ProductDetailAPIView.as_view(), name="product-detail")
]
