from django.urls import path
from .views import PostsList, PostDetail, PostSearch, NewsCreate, PostUpdate, PostDelete, CategoryListView, subscribe

urlpatterns = [
   path('', PostsList.as_view()),
   path('<int:pk>/', PostDetail.as_view()),
   path('search/', PostSearch.as_view(), name='search'),
   path('create/', NewsCreate.as_view(), name='news_create'),
   path('articles/create/', NewsCreate.as_view(), name='article_create'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('articles/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]
