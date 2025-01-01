from django import forms
from django_filters import FilterSet, CharFilter, DateFilter, ModelChoiceFilter
from .models import Author

class PostFilter(FilterSet):
    title = CharFilter(
        label='Title',
        lookup_expr='iregex'
    )

    author__user__username = ModelChoiceFilter(
        empty_label = 'Not selected',
        label = 'Author',
        queryset = Author.objects.all()
    )

    created_time = DateFilter(
        widget = forms.DateInput(attrs={'type': 'date'}),
        label='Created date',
        lookup_expr='date__gte'
    )
