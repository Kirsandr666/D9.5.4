from django_filters import FilterSet, ModelChoiceFilter
from .models import Post, Author, Category
from django_filters import DateFilter
from .forms import *


class PostFilter(FilterSet):
   topic = ModelChoiceFilter(field_name='category', queryset=Category.objects.all(), label='Категория поста', empty_label='любая')
   author = ModelChoiceFilter(field_name='author', queryset=Author.objects.all(), label='Автор', empty_label='любой')
   date = DateFilter(field_name='date_in', widget=forms.DateInput(attrs={'type': 'date'}), label='Позже даты',
                      lookup_expr='date__gte')


class Meta:
    model = Post
    fields = {
        'title': ['icontains'],
        'author' : ['exact'],
    }
