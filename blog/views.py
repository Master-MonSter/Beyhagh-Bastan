from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, PostImage, Comment
from .forms import CommentForm
from django.contrib import messages
from django.db.models import Q

def dark_light_switch(request):
    if 'dark' in request.path:
        return ('dark')
    return ('light')

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
            posts = posts.filter(Q(content_1__contains=x) | Q(content_2__contains=x))
    # Search validations *************************************************************************************
            
    # Deleting duplicated values from tag and category ********************************************************************
    tag_con = []
    cat_con = []
    for post in posts:
        for tag in post.tag.all():
            tag_con.append(str(tag))
        for cat in post.category.all():
            cat_con.append(str(cat))
    tag_con = list(dict.fromkeys(tag_con))
    cat_con = list(dict.fromkeys(cat_con))
    # Deleting duplicated values from tag and category ********************************************************************

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

    context = {'context': posts, 'tag_con': tag_con, 'cat_con': cat_con}
    return render(request, 'blog/light/blog.html', context)

def blog_single_view(request, pid):
    # ******************************** About CommentForm ********************************
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'دیدگاه شما با موفقیت ثبت گردید')
            form.save()
        else:
            messages.add_message(request, messages.ERROR, 'متاسفانه دیدگاه شما ثبت نشد')
    form = CommentForm()
    # ******************************** About CommentForm ********************************

    posts = check_published_date()
    context = get_object_or_404(posts, pk=pid)
    if context.login_require == True and not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, 'You are not logged in<br>Please login')
        # return redirect('accounts:login', 'blog:index')
        return redirect(f"/accounts/{dark_light_switch(request)}/login/?next=" + request.path)
    comments = Comment.objects.filter(post=context.id, approved = True)
    context.counted_views = context.counted_views + 1
    context.save()
    # Finding the post before and after
    nextPost = posts.filter(pk__gt=pid).first()
    prevPost = posts.filter(pk__lt=pid).last()
    images = PostImage.objects.filter(post_id=pid)
    context = {'context': context, 'prevPost': prevPost, 'nextPost': nextPost, 'comments': comments, 'form': form, 'images': images}
    # context = {'context': context, 'prevPost': prevPost, 'nextPost': nextPost, 'images': images}
    # return render(request, 'blog/blog-single.html', context)
    return render(request, 'blog/light/blog-single.html', context)


