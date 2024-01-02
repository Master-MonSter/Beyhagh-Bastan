from django.urls import path
from . import views

app_name = 'light_mode'

# It is useable when that moved on db
# Debug is False
# from django.conf.urls import handler404
# handler404 = 'light_mode.views.custom_404'

urlpatterns = [
    # ********************************************* Home pages ****************************************
    path('light/', views.index_carousel2_view, name='index_carousel2'),
    path('dark/', views.index_carousel2_view, name='index_carousel2_dark'),
    # path('', views.index_slider_view, name='index_slider'),
    # path('', views.index_carousel_view, name='index_carousel'),
    # path('', views.index_video_view, name='index_video'),
    # path('', views.index_imagesGrid_view, name='index_imagesGrid'),
    # ********************************************* Home pages ****************************************

    path('light/404_error_page/', views.error_page_404, name='404_error_page'),

    path('light/about/', views.about_view, name='about'),
    path('dark/about/', views.about_view, name='about_dark'),
    path('light/contact/', views.contact_view, name='contact'),
    path('dark/contact/', views.contact_view, name='contact_dark'),
    path('newsletter', views.newsletter_view, name='news_letter'),
]