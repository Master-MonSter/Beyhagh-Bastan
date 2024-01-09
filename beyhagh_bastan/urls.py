"""
URL configuration for beyhagh_bastan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from light_mode.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap_single_post, BlogSitemap_category, BlogSitemap_tag
from portfolio.sitemaps import PortfolioSitemap_portfolio, PortfolioSitemap_category, PortfolioSitemap_tag

sitemaps = {
    # It seems that the app name is not important.
    "static": StaticViewSitemap,
    
    # Blog
    "blog_single_post": BlogSitemap_single_post,
    "blog_category": BlogSitemap_category,
    "blog_tag": BlogSitemap_tag,
    
    # Portfolio
    "portfolio_portfolio": PortfolioSitemap_portfolio,
    "portfolio_category": PortfolioSitemap_category,
    "portfolio_tag": PortfolioSitemap_tag,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('light_mode.urls')),
    path('blog/', include('blog.urls')),
    path('captcha/', include('captcha.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('accounts.urls')),
    path('portfolio/', include('portfolio.urls')),
    path(
    "sitemap.xml",
    sitemap,
    {"sitemaps": sitemaps},
    name="django.contrib.sitemaps.views.sitemap",),
    path('robots.txt', include('robots.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
