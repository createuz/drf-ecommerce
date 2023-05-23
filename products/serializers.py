from rest_framework import serializers
from .models import Product, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'created_at']


class ProductSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'category', 'description', 'color',
                  'original_price', 'discount', 'main_image', 'image1', 'image2',
                  'image3', 'image4', 'image5', 'image6', 'image7',
                  'image8', 'image9', 'image10', 'comments']
