from rest_framework import serializers
from .models import Product, Category, Comment, ShoppingCard


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializerForCreate(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializerForCard(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'price', 'category')


class ShoppingCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCard
        fields = ('product', 'quantity', 'user', 'date')


class ShoppingCardForDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializerForCard()

    class Meta:
        model = ShoppingCard
        fields = ('product', 'quantity')


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
