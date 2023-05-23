from django.urls import path
from .views import ProductListCreateView, ProductUpdateDeleteView, ProductDetailView

urlpatterns = [
    path('product/', ProductListCreateView.as_view(), name='product-list-create'),
    path('product-update-delete/<int:pk>', ProductUpdateDeleteView.as_view(), name='products_update_delete'),
    path('product-detail/<int:pk>', ProductDetailView.as_view(), name='products_detail'),

]
from django.urls import path
from .views import ProductListCreateView, ProductUpdateDeleteView
#
# urlpatterns = [
#     path('product/', ProductListCreateView.as_view(), name='product-list-create'),
#     path('product/<int:pk>/', ProductUpdateDeleteView.as_view(), name='product-update-delete'),
#     # path('product/on_sale/', OnSaleProductListView.as_view(), name='on-sale-product-list'),
# ]