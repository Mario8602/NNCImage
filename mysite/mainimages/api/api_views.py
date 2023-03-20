from rest_framework.generics import ListAPIView

from .serializers import CategorySerializer, PostSerializer
from ..models import Category, Post


class CategoriesListAPIView(ListAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class PostListAPIview(ListAPIView):

    serializer_class = PostSerializer
    queryset = Post.objects.all()