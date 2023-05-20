from django.urls import path

from .views import ProductAPIView, ProductUpdateDeleteAPIView, DetailAPIView

urlpatterns = [
    path('products/', ProductAPIView.as_view(), name='products'),
    path('product-update-delete/<int:pk>', ProductUpdateDeleteAPIView.as_view(), name='products_update_delete'),
    path('details/', DetailAPIView.as_view(), name='details'),
    path('category/', Category.as_view(), name='category'),
]
