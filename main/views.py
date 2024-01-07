from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from main.forms import ContactForm, NewsLetterForm
from django.contrib import messages

# Create your views here.
def index_view(request):
    return render(request, 'main/index.html')

def comming_soon_view(request):
    if request.method == 'POST':
        msg = ""
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, '************** فرم شما با موفقیت ثبت شد **************')
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
    return render(request, 'main/coming_soon/comingsoon-countdown-bubble.html')
    # return render(request, 'main/coming_soon/comingsoon-countdown-particel.html')


def newsletter_view(request):
    if request.method == 'POST':
        msg=""
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, '**************** ایمیل شما با موفقیت ثبت شد ***************')
            return render(request, 'main/coming_soon/comingsoon-countdown-bubble.html')
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
    return render(request, 'main/coming_soon/comingsoon-countdown-bubble.html')

