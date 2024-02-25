from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import AbstractUser


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
    photo = models.ImageField(default='mysite/media/profiles/default.png', upload_to='profiles/')
    website = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили пользователей'
