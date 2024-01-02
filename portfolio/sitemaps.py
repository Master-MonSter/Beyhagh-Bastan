from django.contrib.sitemaps import Sitemap
from portfolio.models import Product, Category, Tag


class PortfolioSitemap_portfolio(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Product.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.id
    
class PortfolioSitemap_category(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.id
    
class PortfolioSitemap_tag(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Tag.objects.all()

    def lastmod(self, obj):
        return obj.id
    
    
    
    