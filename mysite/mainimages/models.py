from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager

from django.db import models
from django.urls import reverse

# from players.models import CustomUser

from players.models import CustomUser


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    body = models.TextField(max_length=200, blank=True, verbose_name='Контент')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    last_modified = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    categorys = models.ManyToManyField('Category', related_name='categorys1')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_post', blank=True, null=True)

    def __str__(self):
        return f'{self.title} {self.body}'

    def get_absolute_url(self):
        return reverse('post_selection', kwargs={'pk': self.pk})


class Category(models.Model):
    categories = models.CharField(max_length=20, db_index=True, verbose_name='Категории')

    def __str__(self):
        return f'{self.categories}'


# class User(AbstractBaseUser):
#     email = models.EmailField(max_length=100, unique=True)
#     username = models.CharField(max_length=100, unique=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']
#
#     def __str__(self):
#         return f'{self.email}'
#
#
# class Profile(models.Model):
#     first_name = models.CharField(max_length=40)
#     last_name = models.CharField(max_length=40)
#     description = models.TextField()
#     photo = models.ImageField(default='default.png', upload_to='user_photos/%Y/%m/%d')
#
#     def __str__(self):
#         return f'{self.user.username}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment1')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    body = models.TextField(max_length=300, verbose_name='Контент')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'SAYS {self.body}'


class GroupsPosts(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='group_user')
    posta = models.ManyToManyField(Post, related_name='posta', blank=True)
    title = models.CharField(max_length=300)
    cover = models.ImageField(upload_to='photos/groups/%Y/%m/%d', verbose_name='Ковёр')
    body = models.TextField(blank=True)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('open_group', kwargs={'title': self.title})