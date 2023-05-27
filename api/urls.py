from django.urls import path
from rest_framework.routers import DefaultRouter

# from .views import ProductAPIView, AddToShoppingCardAPIView, UserShoppingCardAPIView, \
#     DeleteFromCardAPIView, ProductListCreateView, ProductUpdateDeleteView, ProductDetailView, CommentCreateView, \
#     SendMail
#
# urlpatterns = [
#     path('api/', ProductAPIView.as_view(), name='api'),
#     path('add_product/', ProductListCreateView.as_view(), name='product-list-create'),
#     path('product-update-delete/<int:pk>', ProductUpdateDeleteView.as_view(), name='products_update_delete'),
#     path('product-detail/<int:pk>', ProductDetailView.as_view(), name='products_detail'),
#     path('product/comment/<int:pk>', CommentCreateView.as_view(), name='comment-create'),
#     path('product/on_sale/', ProductListCreateView.as_view(), name='on-sale-product-list'),
#     path('add-to-card', AddToShoppingCardAPIView.as_view(), name='shopping_card'),
#     path('send-email', SendMail.as_view(), name='send_email'),
#     path('user-card', UserShoppingCardAPIView.as_view(), name='user_card'),
#     path('user-card-delete/<int:pk>', DeleteFromCardAPIView.as_view(), name='user_card_delete'),
#
# ]
# from api.views import ProductViewSet, CategoryViewSet, CommentViewSet
#
# product_list = ProductViewSet.as_view({'get': 'list', 'post': 'create'})
#
# product_detail = ProductViewSet.as_view(
#     {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})
#
# comment_list = CommentViewSet.as_view({'get': 'list', 'post': 'create'})
#
# comment_detail = CommentViewSet.as_view(
#     {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})
#
# category_list = CategoryViewSet.as_view({'get': 'list', 'post': 'create'})
#
# category_detail = CategoryViewSet.as_view(
#     {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})
# from django.urls import path, include
# router = DefaultRouter()
# router.register(r'products', ProductViewSet, basename='product')
# router.register(r'comments', CommentViewSet, basename='comment')
# router.register(r'categories', CategoryViewSet, basename='category')
#
#
#
# urlpatterns = [
#     path('products/', product_list, name='product-list'),
#     path('products/<int:pk>/', product_detail, name='product-detail'),
#     path('categories/', category_list, name='category-list'),
#     path('categories/<int:pk>/', category_detail, name='category-detail'),
#     path('products/comment/<int:pk>', product_detail, name='product-comment'),
#     path('comments/', comment_list, name='comment-list'),
#     path('comments/<int:pk>/', comment_detail, name='comment-detail'),
#     path('', include(router.urls)),
#
# ]

#
# from api.views import ProductViewSet, CategoryViewSet, CommentViewSet
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register(r'products', ProductViewSet, basename='product')
# router.register(r'comments', CommentViewSet, basename='comment')
# router.register(r'categories', CategoryViewSet, basename='category')
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, ProductViewSet, ShoppingCardViewSet, SendMailViewSet
)

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'shopping-cards', ShoppingCardViewSet)
router.register(r'send-mail', SendMailViewSet, basename='send-mail')

urlpatterns = [
    path('', include(router.urls)),
]
