from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, ProductViewSet, SendMail, AddToShoppingCardAPIView,
    UserShoppingCardAPIView, DeleteFromCardAPIView, UserShoppingLikeAPIView, DeleteFromLikeAPIView,
    AddToShoppingLikeAPIView, SearchAPIView, BlogDetailAPIView
)

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')
# router.register(r'comments', CommentViewSet, basename='comment')


urlpatterns = [

    # Products
    path('products/', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='product-list'),
    path('products/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='product-detail'),

    # Categories
    path('categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list'),
    path('categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='category-detail'),

    # Send Email
    path('send-email/', SendMail.as_view(), name='send_email'),
    path('add-to-card', AddToShoppingCardAPIView.as_view(), name='shopping_card'),
    path('user-card', UserShoppingCardAPIView.as_view(), name='user_card'),
    path('user-card-delete/<int:pk>', DeleteFromCardAPIView.as_view(), name='user_card_delete'),
    path('add-to-like', AddToShoppingLikeAPIView.as_view(), name='shopping_like'),
    path('user-like', UserShoppingLikeAPIView.as_view(), name='user_like'),
    path('user-like-delete/<int:pk>', DeleteFromLikeAPIView.as_view(), name='user_like_delete'),
    path('', include(router.urls)),

    # Search
    path('search/', SearchAPIView.as_view(), name='your-model-list'),

    # Blog
    path('blog/<int:pk>', BlogDetailAPIView.as_view(), name='detail'),
    path('blog-detail/<int:pk>', BlogDetailAPIView.as_view(), name='detail'),
]

'''
    GET /products/: Get a list of products.
    POST /products/: Add new product.
    PUT /products/<pk>/: Update a specific product.
    DELETE /products/<pk>/: Delete a specific product.
    GET /products/<pk>/: Get details of a particular product.
    GET /categories/: Get a list of categories.
    POST /categories/: Add new category.
    PUT /categories/<pk>/: Update a specific category.
    DELETE /categories/<pk>/: Delete a specific category.
'''
