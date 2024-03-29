from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from blog.models import Post, Category, Tag, Comment, PostImage


# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'status', 'login_require', 'author', 'counted_views', 'created_date', 'published_date')
    list_filter = ('status', 'login_require', 'author')
    # It's prefer to Meta class
    # ordering = ('-created_date',) 
    search_fields = ('title', 'content_1', 'content_2')
    summernote_fields = ('content_1', 'content_2')

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'post', 'approved', 'email', 'created_date')
    list_filter = ('post', 'approved')
    # It's prefer to Meta class
    # ordering = ('-created_date',) 
    search_fields = ('name', 'email')

class PostImagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'post')
    list_filter = ('post_id',)
    search_fields = ('name',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostImage, PostImagesAdmin)