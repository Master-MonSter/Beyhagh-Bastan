# sitemaps.py
from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ["light_mode:index_carousel2", "light_mode:index_carousel2_dark", "light_mode:about", "light_mode:about_dark", "light_mode:contact", "light_mode:contact_dark"]

    def location(self, item):
        return reverse(item)