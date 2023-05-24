from rest_framework import serializers
from .models import Product, Comment
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import Product, Category, ShoppingCard


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'created_at']


class ProductSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializerForCreate(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializerForCard(ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'price', 'category')


class ShoppingCardSerializer(ModelSerializer):
    class Meta:
        model = ShoppingCard
        fields = ('product', 'quantity', 'user', 'date')


class ShoppingCardForDetailSerializer(ModelSerializer):
    product = ProductSerializerForCard()

    class Meta:
        model = ShoppingCard
        fields = ('product', 'quantity')
