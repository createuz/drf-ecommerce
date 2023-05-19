import datetime
from datetime import timedelta, datetime

from django.db.models import Q
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Product
from .permission import IsAuthenticatedOrReadOnly2
from .serializers import ProductSerializer, ProductSerializerForCreate


class ProductAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly2,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        elif self.request.method == 'POST':
            return ProductSerializerForCreate

    def get_permission_classes(self):
        if self.request.method == 'GET':
            return tuple()
        else:
            return (IsAuthenticated,)


class ProductUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.filter()
    serializer_class = ProductSerializer
    permission_classes = ()
