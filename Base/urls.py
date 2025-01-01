from django.urls import path
from .views import (
    PostList, PostDetail, PostListSearch, CreatePost, UpdatePost, DeletePost
)

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', PostListSearch.as_view(), name='post_list_search'),
    path('news/create/', CreatePost.as_view(), name='post_create_news'),
    path('news/<int:pk>/edit/', UpdatePost.as_view(), name='post_edit_news'),
    path('news/<int:pk>/delete/', DeletePost.as_view(), name='post_delete_news'),
    path('articles/create/', CreatePost.as_view(), name='post_create_article'),
    path('articles/<int:pk>/edit/', UpdatePost.as_view(), name='post_edit_article'),
    path('articles/<int:pk>/delete/', DeletePost.as_view(), name='post_delete_article'),
]