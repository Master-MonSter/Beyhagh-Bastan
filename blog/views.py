from django.shortcuts import render

# Create your views here.
def index_light_view(request):
    return render(request, 'blog/light/blog.html')

def blog_single_light_view(request):
    return render(request, 'blog/light/blog-single.html')