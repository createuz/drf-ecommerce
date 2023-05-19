from rest_framework.serializers import ModelSerializer

from .models import Product, Detail, Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializerForCreate(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class Detailserializer(ModelSerializer):
    class Meta:
        model = Detail
        fields = '__all__'
