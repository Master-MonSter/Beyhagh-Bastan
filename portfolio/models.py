from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("portfolio:category_light", kwargs={"cat_name": self.name})


# I don't use taggit here because it dosent work for persian words so I create a Tag model same Category model       
class Tag(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("portfolio:tag_light", kwargs={"tag_name": self.name})

class Product(models.Model):
    # *** Attention *** for using (Char field) or (Text field) for setting empty in these it's better don't use null=True just use blank=True Because django use in two case 2values("", None)
    image_main = models.ImageField(upload_to = 'portfolio/', default='portfolio/default.jpg')
    product_id = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, blank=True)
    product_age = models.IntegerField(blank=True, null=True)
    dimensions = models.CharField(max_length=255, blank=True)
    material = models.CharField(max_length=255, blank=True)
    weight = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=255, blank=True)
    price = models.FloatField(blank=True, null=True)
    info = models.TextField()
    more_info = models.TextField(blank=True)
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
        return reverse('portfolio:portfolio_single_light', kwargs={'pid': self.id})
    
# Created for Posts' images excluded image-main
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'product/')

    class Meta:
        ordering = ['product']

    def __str__(self):
        return self.image.url

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
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