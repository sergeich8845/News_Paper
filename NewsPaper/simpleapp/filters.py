import django_filters
from .models import News
from django import forms

class NewsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Название')
    author = django_filters.CharFilter(lookup_expr='icontains', label='Автор')
    publication_date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}), label='Дата после')

    class Meta:
        model = News
        fields = ['title', 'author', 'publication_date']