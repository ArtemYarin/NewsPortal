from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Author

class PostForm(forms.ModelForm):
    title = forms.CharField(min_length=10)
    text = forms.CharField(min_length=64)
    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label='')

    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'author',
            'category',
        ]
