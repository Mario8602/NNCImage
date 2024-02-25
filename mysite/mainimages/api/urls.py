from django.urls import path

from .api_views import CategoriesListAPIView, PostListAPIview

urlpatterns = [
    path('categories/', CategoriesListAPIView.as_view(), name='categories'),
    path('posts/', PostListAPIview.as_view(), name='posts'),
]
