from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

def check_published_date():
    # Now time with timezone
    now = datetime.now()
    now = timezone.make_aware(datetime(now.year, now.month, now.day, now.hour, now.minute, now.second))
    # Now time without timezone
    # now = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
    posts = Post.objects.filter(published_date__lte=now, status=1)
    return posts

# Create your views here.
def index_view(request, **kwargs):
    posts = check_published_date()
    # Category validation ***********************************************************************************
    if kwargs is not None:
        if kwargs.get('cat_name') is not None:
            posts = posts.filter(category__name=kwargs['cat_name'])
        elif kwargs.get('author_username') is not None:
            posts = posts.filter(author__username=kwargs['author_username'])
        elif kwargs.get('tag_name') is not None:
            posts = posts.filter(tag__name=kwargs['tag_name'])
    # Category validation ***********************************************************************************
    # Search validations *************************************************************************************
    if request.method == 'GET':
        if x:= request.GET.get('sBar'):
            posts = posts.filter(content__contains=x)
    # Search validations *************************************************************************************
    # Pagination *********************************************************************************************
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except EmptyPage:
        posts = posts.get_page(1)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    # Pagination *********************************************************************************************

    context = {'context': posts}
    return render(request, 'blog/light/blog.html', context)

def blog_single_view(request):
    return render(request, 'blog/light/blog-single.html')