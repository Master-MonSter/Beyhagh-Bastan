from django.urls import path
from . import views
# from blog.feeds import LatestEntriesFeed
from django.contrib.auth import views as auth_views

app_name = 'portfolio'

urlpatterns = [
    path('light/', views.index_view, name='portfolio_light'),
    path('dark/', views.index_view, name='portfolio_dark'),
    path('light/category-<str:cat_name>', views.index_view, name='category_light'),
    path('dark/category-<str:cat_name>', views.index_view, name='category_dark'),
    path('light/tag-<str:tag_name>', views.index_view, name='tag_light'),
    path('dark/tag-<str:tag_name>', views.index_view, name='tag_dark'),
    path('search/', views.index_view, name='search'),
    path('light/single-<int:pid>', views.portfolio_single_view, name='portfolio_single_light'),
    path('dark/single-<int:pid>', views.portfolio_single_view, name='portfolio_single_dark'),
]
    