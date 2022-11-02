from django.urls import path

from . import views
from .views import PostDeleteView


urlpatterns = [
    path('', views.posts, name='postes'),
    path('<int:pk>/', views.post_selection, name='post_selection'),
    # path('<int:id>/delete-post', views.delete_post, name='delete_post'),
    path('create_post/', views.create_post, name='create_post_one'),
    path('home_page/', views.home_page, name='home_page'),
    path('home_page_create/', views.home_page_create, name='home_page_create'),
    path('group/<str:title>/', views.open_group, name='open_group'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete')
]