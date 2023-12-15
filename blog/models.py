from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

# I don't use taggit here because it dosent work for persian words so I create a Tag model same Category model       
class Tag(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image_main = models.ImageField(upload_to = 'blog/', default='blog/default.jpg')
    image_content_1 = models.ImageField(upload_to = 'blog/', default='blog/image_content.png')
    image_content_2 = models.ImageField(upload_to = 'blog/', default='blog/image_content.png')
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    content_1 = models.TextField()
    content_2 = models.TextField()
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tag)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    login_require = models.BooleanField(default=False)
    published_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_date'] # ['created_date'] reverse_order
        # How to change name of the class
        # verbose_name = 'پست'
        # verbose_name_plural = 'پست ها'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'pid': self.id})
    
# Created for Posts' images excluded image-main
class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'blog/')

    class Meta:
        ordering = ['post']

    def __str__(self):
        return self.image.url
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name

