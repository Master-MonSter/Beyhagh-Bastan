from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    # path('', views.comming_soon_view, name='coming_soon_index'),
    path('', views.index_view, name='index'),
    path('newsletter', views.newsletter_view, name='news_letter'),
]