from django.urls import path
from .views import ProductAPIView, AddToShoppingCardAPIView, UserShoppingCardAPIView, \
    DeleteFromCardAPIView, ProductListCreateView, ProductUpdateDeleteView, ProductDetailView, CommentCreateView

urlpatterns = [
    path('products/', ProductAPIView.as_view(), name='products'),
    path('add_product/', ProductListCreateView.as_view(), name='product-list-create'),
    path('product-update-delete/<int:pk>', ProductUpdateDeleteView.as_view(), name='products_update_delete'),
    path('product-detail/<int:pk>', ProductDetailView.as_view(), name='products_detail'),
    path('product/comment/<int:pk>', CommentCreateView.as_view(), name='comment-create'),
    path('product/on_sale/', ProductListCreateView.as_view(), name='on-sale-product-list'),
    path('add-to-card', AddToShoppingCardAPIView.as_view(), name='shopping_card'),
    path('user-card', UserShoppingCardAPIView.as_view(), name='user_card'),
    path('user-card-delete/<int:pk>', DeleteFromCardAPIView.as_view(), name='user_card_delete'),

]

