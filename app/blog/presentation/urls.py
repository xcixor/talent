from django.urls import path
from blog.presentation.views import (
    PostsHomeView, PostDetailView, BlogSearchView,
    ClearBlogSearchView)

app_name = 'blog'

urlpatterns = [
    path('', PostsHomeView.as_view(), name='posts'),
    path('search/', BlogSearchView.as_view(), name='blog_search'),
    path('clear/search/', ClearBlogSearchView.as_view(), name='clear_search'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]
