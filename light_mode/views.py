from django.shortcuts import render

# Create your views here.

# ************************************************* Indexes ************************************************
def index_carousel_view(request):
    return render(request, 'light/index.html')

def index_slider_view(request):
    return render(request, 'light/index2.html')

def index_imagesGrid_view(request):
    return render(request, 'light/index3.html')

def index_carousel2_view(request):
    return render(request, 'light/index4.html')

def index_video_view(request):
    return render(request, 'light/index5.html')
# ************************************************* Indexes ************************************************

# ************************************************* portfolios ************************************************
def portfolio_horizontal_view(request):
    return render(request, 'light/portfolio.html')

def portfolio_vertical_view(request):
    return render(request, 'light/portfolio2.html')

def portfolio_column_view(request):
    return render(request, 'light/portfolio3.html')

def portfolio_single_view(request):
    return render(request, 'light/portfolio-single.html')

def portfolio_single2_view(request):
    return render(request, 'light/portfolio-single2.html')

def portfolio_single3_view(request):
    return render(request, 'light/portfolio-single3.html')

def portfolio_single4_view(request):
    return render(request, 'light/portfolio-single4.html')
# ************************************************* portfolios ************************************************



def about_view(request):
    return render(request, 'light/about.html')

def blog_view(request):
    return render(request, 'light/blog.html')

def blog_single_view(request):
    return render(request, 'light/blog-single.html')

def contact_view(request):
    return render(request, 'light/contacts.html')




