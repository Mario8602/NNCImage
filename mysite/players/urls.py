from django.urls import path

from .views import (SignUpView, user_login,
                    user_profile, ShowProfilePageView,
                    CreateProfilePageView, profile, ProfileUpdateView)


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', user_login, name='login'),
    path('profile/', user_profile, name='profile'),
    path('user_profile/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_user_profile'),
    path('profile_re/', profile, name='re_profile'),
    path('user_profile/<int:pk>/update', ProfileUpdateView.as_view(), name='update'),
    # path('edit_profile/', user_edit_profile, name='edit_profile'),
    # path('profile/', profile, name='profile'),
    # path('test_celery/', )
]