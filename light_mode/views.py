from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from light_mode.forms import ContactForm, NewsLetterForm
from django.contrib import messages

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

def contact_view(request):
    # *********************************** Get full path ********************************
    # full_path = request.get_full_path()
    # path_info = request.path_info
    path_info = request.path
    # *********************************** Get full path ********************************
    light_theme = "light" in path_info
    print(path_info)
    print(light_theme)
    # request.add({"names": 'ali' })
    updated_request = request.GET.copy()
    print(request)
    if request.method == 'POST':
        msg = ""
        form = ContactForm(request.POST)
        if form.is_valid():
            # Update values before save ****************************************************************
            # obj = form.save(commit=False)
            # obj.name = "unknown"
            # Update values before save ****************************************************************
            form.save()
            messages.add_message(request, messages.SUCCESS, '******************<br>Well done<br>******************')
            print(messages)
            # return HttpResponseRedirect('/contact')
        else:
            # ************************************** Set error list ***********************************************
            if form.errors:
                for field in form.errors:
                    print(form.errors)
                    for error in form.errors[field]:
                        msg = msg + f"<p><b>{field}:</b> {error}</p>"
            # messages.add_message(request, messages.ERROR, 'Somthing went wrong<br>please try again')
            messages.add_message(request, messages.ERROR, msg)
            # ************************************** Set error list ***********************************************
    form = ContactForm()
    return render(request, 'light/contacts.html', {'form': form, 'light_theme': light_theme})

def newsletter_view(request):
    if request.method == 'POST':
        msg=""
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, '******************<br>Well done<br>******************')
            return HttpResponseRedirect(request.POST.get('path'))
        else:
            # ************************************** Set error list ***********************************************
            if form.errors:
                for field in form.errors:
                    print(form.errors)
                    for error in form.errors[field]:
                        msg = msg + f"<p><b>{error} </b> :{field}</p>"
            # messages.add_message(request, messages.ERROR, 'Somthing went wrong<br>please try again')
            messages.add_message(request, messages.ERROR, msg)
            # ************************************** Set error list ***********************************************
    return HttpResponseRedirect(request.POST.get('path'))


