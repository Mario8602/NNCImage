from django import forms
from .models import Comment, Post, GroupsPosts


class CommentForm(forms.ModelForm):

    body = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'comment here...',
        'rows': 2,
    }))

    class Meta:
        model = Comment
        fields = ['body']


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
        fields = ['title', 'is_private', 'cover', 'posta', 'body']

    def __init__(self, *args, **kwargs):
        super(CreateGroupForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'title'
        self.fields['body'].widget.attrs['class'] = 'md-textarea form-control'
        self.fields['cover'].widget.attrs['class'] = 'form-control'
        self.fields['posta'].widget.attrs['class'] = 'md-textarea form-control'
        for visible in self.visible_fields():
            if visible.name == 'title':
                visible.field.widget.attrs['class'] = 'form-control border rounded-pill p-2 mt-1'


class SaveToGroupForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = []
