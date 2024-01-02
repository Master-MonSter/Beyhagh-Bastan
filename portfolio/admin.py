from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product, Category, Tag, Comment, ProductImage


# Register your models here.
class ProductAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'sub_title', 'product_id', 'weight', 'price', 'status', 'login_require', 'counted_views', 'created_date', 'published_date')
    list_filter = ('status', 'login_require')
    search_fields = ('title', 'info', 'product_id')
    summernote_fields = ('info', 'more_info')

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'product', 'approved', 'email', 'created_date')
    list_filter = ('product', 'approved')
    search_fields = ('name', 'email')

class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'product')
    list_filter = ('product_id',)
    search_fields = ('name',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImagesAdmin)