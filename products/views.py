from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, Detail
from .permission import IsAuthenticatedOrReadOnly2
from .serializers import ProductSerializer, ProductSerializerForCreate, Detailserializer


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


class DetailAPIView(APIView):
    def get(self, request):
        products = Detail.objects.all()
        products_data = Detailserializer(products, many=True)
        return Response(products_data.data)

    def post(self, request):
        product_data = Detailserializer(data=request.data)
        product_data.is_valid(raise_exception=True)
        product_data.save()
        return Response(status=201)
