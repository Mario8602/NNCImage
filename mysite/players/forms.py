from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.forms import ModelForm

from .models import CustomUser, ProfileUser


class CustomUserCreationForm(UserCreationForm):

    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя профиля'
    }))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите адрес эл. почты'
    }))
    phone = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите номер телефона',
    }))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Создайте пароль'
    }))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Подтверждение пароля'
    }))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone')
        # widgets = {
        #     'username': forms.TextInput(),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'phone': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        # }


class CustomUserChangeForm(UserChangeForm):

    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя профиля'
    }))

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Создайте пароль'
    }))

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя профиля'
    }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль'
    }))


# class EditProfileForm(ModelForm):
#     photo = forms.ImageField(required=False, widget=forms.FileInput)
#     username = forms.CharField(widget=forms.TextInput)
#
#     class Meta:
#         model = ProfileUser
#         fields = ['photo', 'first_name', 'last_name', 'date_of_birth', 'website']
#
#     def __init__(self, *args, **kwargs):
#         super(EditProfileForm, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             if visible.name == 'website':
#                 visible.field.widget.attrs['class'] = 'edit-profile-input form-control about-input'
#             else:
#                 visible.field.widget.attrs['class'] = 'edit-profile-input form-control rounded-pill'


# class UserEditForm(forms.ModelForm):
#     username = forms.CharField(required=True)
#     email = forms.EmailField(required=True)
#     first_name = forms.CharField(required=False)
#     last_name = forms.CharField(required=False)
#
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'username', 'email']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    first_name = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = ProfileUser
        fields = ['photo', 'first_name']


class ProfileUpdateForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control1',
        'rows': 1,
        'title': 'Your name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'title': 'Им яыфвфыв',
        'class': 'form-control1',
        'rows': 1,
    }))
    photo = forms.ImageField(widget=forms.FileInput(attrs={
        'name': 'attached_file',
        'class': 'form-control mb-3',
    }))

    website = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control2', 'rows': 1}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control2', 'rows': 1}))
    about = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control2', 'rows': 5}))

    class Meta:
        model = ProfileUser
        fields = ['first_name', 'last_name', 'photo', 'website', 'date_of_birth', 'about']


class ProfileCreateForm(forms.ModelForm):

    photo = forms.ImageField(widget=forms.FileInput(attrs={
        'name': 'attached_file',
        'class': 'form-control',
        'placeholder': 'Фото',

    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'rows': 1,
        'title': 'Your name',
        'placeholder': 'Введите имя',
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'title': 'Фамилия',
        'class': 'form-control',
        'rows': 1,
        'placeholder': 'Введите фамилию',
    }))

    website = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'rows': 1,
        'placeholder': 'Введите ссылку',
    }))

    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'rows': 1,
        'placeholder': 'Введите дату рождения',
    }))

    about = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 5,
        'placeholder': 'Введите информацию о себе'
    }))


    class Meta:
        model = ProfileUser
        fields = ['first_name', 'last_name', 'photo', 'website', 'date_of_birth', 'about']