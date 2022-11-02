from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import AbstractUser

# from .managers import UserManager


# class MyUser(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(, max_length=250, unique=True)
#     email = models.EmailField(null=True, blank=True)
#     phone = models.CharField(max_length=30, null=True, blank=True)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     is_active = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_verified = models.BooleanField(default=False)
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']
#
#     class Meta:
#         verbose_name = 'user'
#         verbose_name_plural = 'users'
#         unique_together = ('username', 'email', 'phone')

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=200, null=True)
    # add additional fields in here
    pass

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class ProfileUser(models.Model):
    user = models.OneToOneField(CustomUser, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(default='profiles/default.png', upload_to='profiles/')
    website = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user}"
        # return f'{self.user.username} profile'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили пользователей'
