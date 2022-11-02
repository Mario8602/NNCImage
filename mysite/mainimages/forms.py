from django import forms
from .models import Comment, Post, Category, GroupsPosts


# class CommentForm(forms.ModelForm):
#
#     author = forms.CharField(widget=forms.Textarea(attrs={
#         'class': 'form-control',
#         'placeholder': 'username...',
#         'rows': 1,
#     }))
#
#     body = forms.CharField(widget=forms.Textarea(attrs={
#         'class': 'md-textarea form-control',
#         'placeholder': 'comment here...',
#         'rows': 4,
#     }))
#
#     class Meta:
#         model = Comment
#         # fields = ('content',)
#         fields = ('author', 'body')


class CommentForm(forms.ModelForm):

    body = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'comment here...',
        'rows': 2,
    }))

    class Meta:
        model = Comment
        fields = ['body']


'''class CreatePostForm(forms.ModelForm):

    title = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Наименование...',
        'rows': 1,
    }))

    body = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Описание...',
        'rows': 3,
    }))

    categorys = forms.ModelChoiceField(queryset=Category.objects.all(), label='', empty_label='Выберите значение',
                                       widget=forms.Select(attrs={
        'class': 'md-textarea form-control',
    }))

    photo = forms.ImageField(label='Выберите фотографию')
    #
    # categorys = forms.CharField(label='', widget=forms.Select(attrs={
    #     'class': 'form-control form-control-lg  select',
    #     'placeholder': 'Выберите категорию',
    # }))

    class Meta:
        model = Post
        fields = ['photo', 'title', 'body', 'categorys']
        # widgets = {'price': forms.TextInput(attrs={'type': 'range', 'class': 'form-range slider', 'step': '5', 'min': '5', 'max': '500'}),
        #            'categorys': forms.Select(attrs={
        #                'id':'RoomTypeDropDownList',
        #                'class':'form-control form-control-lg  select',
        #                'placeholder': 'Выберите категорию',
        #            })}'''


class CreatePostForm(forms.ModelForm):

    title = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Наименование...',
        'rows': 1,
    }))

    body = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Описание...',
        'rows': 3,
    }))

    photo = forms.ImageField(label='Выберите фотографию')

    class Meta:
        model = Post
        fields = ['photo', 'title', 'body', 'categorys']


class CreateGroupForm(forms.ModelForm):

    class Meta:
        model = GroupsPosts
        fields = ['title', 'cover', 'posta', 'body', 'is_private']

# class CreateGroupForm(forms.ModelForm):
#
#     class Meta:
#         model = GroupsPosts
#         fields = ['title', 'is_private']
#
#     def __init__(self, *args, **kwargs):
#         super(CreateGroupForm, self).__init__(*args, **kwargs)
#         self.fields['title'].widget.attrs['placeholder'] = 'Like "Places to Go" or "Recipes to Make"'
#         for visible in self.visible_fields():
#             if visible.name == 'title':
#                 visible.field.widget.attrs['class'] = 'form-control border rounded-pill p-2 mt-1'
#             else:
#                 visible.field.widget.attrs['class'] = 'form-check-input mt-1 private-checkbox'