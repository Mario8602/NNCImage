from rest_framework import serializers

from ..models import Category, Post


class CategorySerializer(serializers.ModelSerializer):

    categories = serializers.CharField(required=True)

    class Meta:
        model = Category
        fields = ['id', 'categories']


class PostSerializer(serializers.ModelSerializer):

    title = serializers.CharField(required=True)
    body = serializers.CharField(required=True)
    photo = serializers.ImageField(required=True)
    created_at = serializers.DateTimeField(required=True)
    last_modified = serializers.DateTimeField(required=True)
    categorys = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'body', 'photo', 'created_at', 'last_modified', 'categorys']