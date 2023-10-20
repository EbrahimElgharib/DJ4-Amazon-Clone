from django.db import models

from taggit.managers import TaggableManager

from django.contrib.auth.models import User
from django.utils import timezone

from django.utils.translation import gettext_lazy as _

from django.utils.text import slugify

from django.db.models.aggregates import Avg


# Create your models here.

FLAG_TYPES = (
    ('Sale', 'Sale'),
    ('New', 'New'),
    ('Feature', 'Feature'),
)

class Product(models.Model):
    name = models.CharField(_('Name'), max_length=120)
    flag = models.CharField(_('Flag'), max_length=10, choices=FLAG_TYPES)
    image = models.ImageField(_('Image'), upload_to='products')
    price = models.FloatField(_('Price'), )
    sku = models.CharField(_('SKU'), max_length=12)
    subtitle = models.CharField(_('Subtitle'), max_length=300)
    description = models.TextField(_('Description'), max_length=40000)
    quantity = models.IntegerField(_('Quantity'), )
    brand = models.ForeignKey('Brand', verbose_name='Brand', related_name='product_brand', on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(null=True, blank=True)
    
    tags = TaggableManager()
    


    def __str__(self):
        return self.name
    
    # instance method ---> apply at each object
    # we used it if we need it always
    

    def get_avg_rate(self):
        avg = self.review_product.aggregate(avg_rate=Avg('rate'))['avg_rate']
        return avg if avg else 0
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
        
    
        
        
    
class ProductImages(models.Model):
    product = models.ForeignKey(Product,verbose_name='Product', related_name='product_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'product_images')
    
    def __str__(self):
        return str(self.product)

class Review(models.Model):
    user = models.ForeignKey(User,verbose_name='User', related_name='review_author', on_delete=models.SET_NULL, null=True )
    product = models.ForeignKey(Product,verbose_name='Product', related_name='review_product', on_delete=models.CASCADE)
    review = models.CharField(_('Review'), max_length=300)
    created_at = models.DateField(_('Created_at'), default=timezone.now)
    rate = models.IntegerField(_('Rate'),)
    
    def __str__(self):
        return f"{self.user} - {self.product}"


class Brand(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    image = models.ImageField(_('Image'), upload_to = 'brands') 
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Brand, self).save(*args, **kwargs)
    
    
    