from django.contrib.sitemaps import Sitemap
from blog.models import Post, Category, Tag


class BlogSitemap_single_post(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.published_date
    
class BlogSitemap_category(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.id
    
class BlogSitemap_tag(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Tag.objects.all()

    def lastmod(self, obj):
        return obj.id
    
    
    
    
    
    
    