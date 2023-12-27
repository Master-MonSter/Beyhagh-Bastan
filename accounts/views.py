from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# ******************************** Change password ********************************
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# ******************************** Change password ********************************

def dark_light_switch(request):
    if 'dark' in request.path:
        return ('dark')
    return ('light')

def next_reload(request):
    # ************************************* This used for next value in login pages *****************************************
    next = ''
    try:
        next = (request.get_full_path()).split("next=")[1]
        return(next)
    except:
        if request.POST.get("next_reload") is not None:
            next = request.POST.get("next_reload")
            return(next)
        else:
            if request.GET.get("next") is not None:
                next = request.POST.get("next")
                return(next)
            return(next)
    # ************************************* This used for next value in login pages *****************************************

def login_view(request):
    next = next_reload(request)       # Save next
    if not request.user.is_authenticated:
        if request.method == 'POST':
            msg=""
            # ********************************************************* Checking that login is done with email or username and handle it *********************************************************
            username = request.POST.get('username')
            password = request.POST.get('password')
            author = User.objects.filter(email=username).first()
            if author is not None:
                request.POST._mutable = True
                request.POST['username'] = author
            form = AuthenticationForm(request=request, data=request.POST)
            # ********************************************************* Checking that login is done with email or username and handle it *********************************************************
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                remember_me = request.POST.get('remember_me')
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    
                    # *********************************** If remember_me was on, means (expiry(Based on sec)) ********************************
                    if remember_me: 
                        request.session.set_expiry(604800) # Here we extend session(a week).
                    else:
                        request.session.set_expiry(0) # The session will be expire after closeing browser
                    # *********************************** If remember_me was on, means (expiry(Based on sec)) ********************************

                    # Checking user that if is logined redirect to next page
                    if user.is_authenticated:
                        messages.add_message(request, messages.SUCCESS, 'خوش آمدید')
                        if next:
                            return redirect(next)
                        else:
                            return redirect('/')
                    # Checking user that if is logined redirect to next page

                    # Maybe this part is expired!
                    # ************************************* Redirect to before post after login else go to home page *************************************
                    # if 'next' in request.POST:
                    #     return redirect(request.POST.get('next'))
                    # else:
                    #     return render('/' + dark_light_switch(request))
                    # ************************************* Redirect to before post after login else go to home page *************************************
           
            # ******************************** Print just form.error_messages[invalid_login] element ********************************
            if form.errors:
                msg = "<p>لطفا نام کاربری و گذرواژه‌ای قابل قبول وارد کنید</p><p>توجه داشته باشید که ممکن است هر دو به کوچکی و بزرگی حروف حساس باشند</p>"
            #     for field in form.errors:
            #         print(field)
            #         for error in form.errors[field]:
            #             print(error)
            #             msg = msg + f"<p>{error}</p>"
            messages.add_message(request, messages.ERROR, msg)
            # ******************************** Print just form.error_messages[invalid_login] element ********************************
        context = {'next_reload': next}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/' + dark_light_switch(request))
        # return redirect(f"/{request.POST.get('style_key')}")

@login_required
def logout_view(request):
    logout(request)
    if 'dark' in request.path:
        return redirect(request.GET.get('next'))
    return redirect(request.GET.get('next'))

def register_view(request):
    next = next_reload(request)       # Save next
    if not request.user.is_authenticated:
        if request.method == 'POST':
            msg=""
            users = ""
            form = UserCreationForm(request.POST)
            users = User.objects.filter(email=request.POST.get('email'))
            if form.is_valid():
                # Update values before save ****************************************************************
                obj = form.save(commit=False)
                obj.email = request.POST.get('email')
                print(users)
                # Update values before save ****************************************************************
                if len(users) == 0:
                    messages.add_message(request, messages.SUCCESS, '.ثبت نام شما با موفقیت انجام شد')
                    form.save()
                    return redirect('/accounts/light/login/?next=' + next)
            if form.errors:
                for field in form:
                    for error in field.errors:
                        msg = msg + f'<p>{error}</p>'
            if len(users) != 0:
                msg = msg + '<p>ایمیل وارد شده تکراری میباشد</p>'
            messages.add_message(request, messages.ERROR, msg)
        context = {'next_reload': next}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/' + dark_light_switch(request))

# **************************************** Some rolls for change password ****************************************
# Your password can’t be too similar to your other personal information.
# Your password must contain at least 8 characters.
# Your password can’t be a commonly used password.
# Your password can’t be entirely numeric.
# **************************************** Some rolls for change password ****************************************
@login_required   
def change_password_view(request):
    next = next_reload(request)       # Save next
    if request.method == 'POST':
        msg = ""
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'رمز عبور شما با موفقیت تغییر کرد')
            if next:
                return redirect(next)
            return redirect('/')
        else:
            if form.errors:
                for field in form.errors:
                    for error in form.errors[field]:
                        msg = msg + f"<p>{error}</p>"
            messages.error(request, msg)
    context = {'next_reload': next}
    return render(request, 'accounts/change_password.html', context)

