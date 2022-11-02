from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, ProfileUser

# from .models import MyUser
#
#
# class MyUserAdmin(admin.ModelAdmin):
#     list_display = ['email', 'username', "phone" ]
#     search_fields = ('username',)
#
#
# admin.site.register(MyUser, MyUserAdmin)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'phone']


class ProfileUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'date_of_birth', 'photo']
    search_fields = ('id', 'user')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ProfileUser, ProfileUserAdmin)
