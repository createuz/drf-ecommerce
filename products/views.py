from rest_framework import status

from django.db.models import Q, Sum
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, ShoppingCard, Category, Comment
from .permission import IsAuthenticatedOrReadOnly2
from .serializers import ProductSerializer, ProductSerializerForCreate, ShoppingCardSerializer, \
    ShoppingCardForDetailSerializer, CategorySerializer, CommentSerializer


class ProductListCreateView(APIView):
    def get(self, request):
        categories = request.GET.getlist('category')
        on_sale = request.GET.get('on_sale', None)

        products = Product.objects.all()

        if categories:
            products = products.filter(category__in=categories)

        if on_sale is not None:
            products = products.filter(on_sale=True)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()

            # Create a comment if provided in the request data
            comment_content = request.data.get('comment', None)
            if comment_content:
                comment = Comment.objects.create(product=product, user=request.user, content=comment_content)

            return Response({'message': 'Product created successfully.'}, status=201)
        return Response(serializer.errors, status=400)


class ProductAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

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


class CommentCreateView(APIView):
    def post(self, request, pk):
        product = Product.objects.filter(id=pk).first()
        if product is None:
            return Response({'message': 'Product not found.'}, status=404)

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product=product, user=request.user)
            return Response({'message': 'Comment created successfully.'}, status=201)
        return Response(serializer.errors, status=400)



class ProductUpdateDeleteView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ProductDetailView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            data = serializer.data

            # Category ni id va name bilan qo'shib qo'yamiz
            category = Category.objects.get(pk=data['category'])
            category_serializer = CategorySerializer(category)
            data['category'] = category_serializer.data

            return Response(data)
        except Product.DoesNotExist:
            return Response({'message': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'message': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product=product, user=request.user)
            return Response({'message': 'Comment created successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryView(APIView):
    def post(self, request):
        product_data = CategorySerializer(data=request.data)
        product_data.is_valid(raise_exception=True)
        product_data.save()
        return Response(status=201)

    def get(self, request):
        products = Category.objects.all()
        products_data = CategorySerializer(products, many=True)
        return Response(products_data.data)





class AddToShoppingCardAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.data._mutable = True
        request.data['user'] = request.user.id
        serializer = ShoppingCardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=201)


class UserShoppingCardAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user_products = ShoppingCard.objects.filter(user=request.user)
        serializer = ShoppingCardForDetailSerializer(user_products, many=True)
        summ = 0
        for element in serializer.data:
            summ += element['product']['price'] * element['quantity']
        data = {
            'data': serializer.data,
            'summ': summ
        }
        return Response(data)


class DeleteFromCardAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        try:
            ShoppingCard.objects.get(Q(pk=pk), Q(user=request.user)).delete()
        except ShoppingCard.DoesNotExist:
            return Response({'message': 'Bunday mahsulot mavjud emas'})
        return Response(status=204)


