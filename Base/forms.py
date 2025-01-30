from datetime import date

from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
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

    def clean(self):
        cleaned_data = super().clean()
        author = cleaned_data.get("author")
        today = date.today()
        today_posts = Post.objects.filter(author=author, created_time__date=today).count()
        if today_posts >= 3:
            raise ValidationError('Post limit is reached')
        return cleaned_data
    

class BasicSignupForm(SignupForm):
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='Common')
        basic_group.user_set.add(user)
        return user
