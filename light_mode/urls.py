from django.urls import path
from . import views

app_name = 'light_mode'

urlpatterns = [
    # ********************************************* Home pages ****************************************
    path('', views.index_carousel2_view, name='index_carousel2'),
    path('', views.index_slider_view, name='index_slider'),
    path('', views.index_carousel_view, name='index_carousel'),
    path('', views.index_video_view, name='index_video'),
    path('', views.index_imagesGrid_view, name='index_imagesGrid'),
    # ********************************************* Home pages ****************************************

    # ********************************************* Portfolios ****************************************
    path('portfolio-horizontal/', views.portfolio_horizontal_view, name='portfolio_horizontal'),
    path('portfolio-vertical/', views.portfolio_vertical_view, name='portfolio_vertical'),
    path('portfolio-column/', views.portfolio_column_view, name='portfolio_column'),

    path('portfolio-single/', views.portfolio_single_view, name='portfolio_single'),
    path('portfolio-single2/', views.portfolio_single2_view, name='portfolio_single2'),
    path('portfolio-single3/', views.portfolio_single3_view, name='portfolio_single3'),
    path('portfolio-single4/', views.portfolio_single4_view, name='portfolio_single4'),
    # ********************************************* Portfolios ****************************************

    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
]