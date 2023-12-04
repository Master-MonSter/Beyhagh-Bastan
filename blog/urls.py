from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('index-light', views.index_light_view, name='index_light'),
    path('blog-single', views.blog_single_light_view, name='blog_single'),
]