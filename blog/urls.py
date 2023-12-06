from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('light/', views.index_light_view, name='index_light'),
    path('dark/', views.index_light_view, name='index_light'),
    path('light/blog-single/', views.blog_single_light_view, name='blog_single'),
    path('dark/blog-single/', views.blog_single_light_view, name='blog_single'),
]