from django.urls import path
from . import views
# from blog.feeds import LatestEntriesFeed
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    # Login
    path('light/login/', views.login_view, name='login_light'),
    path('dark/login/', views.login_view, name='login_dark'),

    # Logout
    path('light/logout/', views.logout_view, name='logout_light'),
    path('dark/logout/', views.logout_view, name='logout_dark'),

    # Register
    path('light/signup/', views.register_view, name='signup_light'),
    path('dark/signup/', views.register_view, name='signup_dark'),
    
    # Password change
    path('light/change_password/', views.change_password_view, name='change_password_light'),
    path('dark/change_password/', views.change_password_view, name='change_password_dark'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset_light'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),

    # path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    # path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    # path('password_reset_confirm/uidb64/token/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    # path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
    