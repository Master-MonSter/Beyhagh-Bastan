from django.urls import path
from . import views
from blog.feeds import LatestEntriesFeed


app_name = 'blog'

urlpatterns = [
    path('light/', views.index_view, name='index_light'),
    path('dark/', views.index_view, name='index_dark'),
    path('light/blog-<int:pid>/', views.blog_single_view, name='blog_single_light'),
    path('dark/blog-<int:pid>/', views.blog_single_view, name='blog_single_dark'),
    path('dark/category-<str:cat_name>', views.index_view, name='category_dark'),
    path('light/category-<str:cat_name>', views.index_view, name='category_light'),
    path('dark/tag-<str:tag_name>', views.index_view, name='tag_dark'),
    path('light/tag-<str:tag_name>', views.index_view, name='tag_light'),
    path('search/', views.index_view, name='search'),
    path("light/rss/feed/", LatestEntriesFeed()),
    # path('light/search/', views.index_view, name='search_light'),
]