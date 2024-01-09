from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, ProductImage, Comment
# from .forms import CommentForm
from django.contrib import messages
from django.db.models import Q

# def index_view(request):
#     return render(request, 'portfolio/portfolio-vertical.html')
# def single_view(request):
#     return render(request, "portfolio/portfolio-single-vertical.html")
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
    products = Product.objects.filter(published_date__lte=now, status=1)
    return products

def index_view(request, **kwargs):
    products = check_published_date()
    # Category validation ***********************************************************************************
    if kwargs is not None:
        if kwargs.get('cat_name') is not None:
            products = products.filter(category__name=kwargs['cat_name'])
        elif kwargs.get('author_username') is not None:
            products = products.filter(author__username=kwargs['author_username'])
        elif kwargs.get('tag_name') is not None:
            products = products.filter(tag__name=kwargs['tag_name'])
    # Category validation ***********************************************************************************
            
    # Search validations *************************************************************************************
    # if request.method == 'GET':
    #     if x:= request.GET.get('sBar'):
    #         products = products.filter(Q(content_1__contains=x) | Q(content_2__contains=x))
    # Search validations *************************************************************************************
            
    # Deleting duplicated values from tag and category ********************************************************************
    tag_con = []
    cat_con = []
    tag_id = []
    for product in products:
        for tag in product.tag.all():
            tag_con.append(str(tag))
            tag_id.append(str(tag.id))
        for cat in product.category.all():
            cat_con.append(str(cat))
    tag_con = list(dict.fromkeys(tag_con))
    cat_con = list(dict.fromkeys(cat_con))
    tag_id = list(dict.fromkeys(tag_id))
    
    zipped_tag_id = zip(tag_con, tag_id)
    
    # Deleting duplicated values from tag and category ********************************************************************

    context = {'products': products, 'tag_con': tag_con, 'cat_con': cat_con, 'zipped_tag_id': zipped_tag_id}
    return render(request, 'portfolio/portfolio-vertical.html', context)
    

def portfolio_single_view(request, pid):
    # ******************************** About CommentForm ********************************
    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         messages.add_message(request, messages.SUCCESS, 'دیدگاه شما با موفقیت ثبت گردید')
    #         form.save()
    #     else:
    #         messages.add_message(request, messages.ERROR, 'متاسفانه دیدگاه شما ثبت نشد')
    # form = CommentForm()
    # ******************************** About CommentForm ********************************

    products = check_published_date()
    context = get_object_or_404(products, pk=pid)
    if context.login_require == True and not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, 'You are not logged in<br>Please login')
        # return redirect('accounts:login', 'blog:index')
        return redirect("/accounts/login/?next=" + request.path)
    # comments = Comment.objects.filter(post=context.id, approved = True)
    context.counted_views = context.counted_views + 1
    context.save()
    # Finding the post before and after
    nextProduct = products.filter(pk__gt=pid).first()
    prevProduct = products.filter(pk__lt=pid).last()
    images = ProductImage.objects.filter(product_id=pid)
    context = {'product': context, 'prevProduct': prevProduct, 'nextProduct': nextProduct, 'images': images}
    # context = {'context': context, 'prevProduct': prevProduct, 'nextProduct': nextProduct, 'comments': comments, 'form': form, 'images': images}
    return render(request, 'portfolio/portfolio-single-vertical.html', context)


