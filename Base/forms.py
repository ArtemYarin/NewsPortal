from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
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

class BasicSignupForm(SignupForm):
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='Common')
        basic_group.user_set.add(user)
        return user
