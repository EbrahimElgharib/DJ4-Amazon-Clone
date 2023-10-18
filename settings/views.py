from django.shortcuts import render

from django.db.models import Count
from product.models import Product, Brand, Review
# Create your views here.


def home(request):
    brand = Brand.objects.all().annotate(produc_count=Count('product_brand'))[:10]
    sold_products = Product.objects.filter(flag='Sale')[:10]
    featured_products = Product.objects.filter(flag='Feature')[:10]
    new_products = Product.objects.filter(flag='New')[:10]
    reviews = Review.objects.filter(rate=5)[:10]
    
    
    context = {
        'brands':brand,
        'sold_products':sold_products,
        'featured_products':featured_products,
        'new_products':new_products,
        'reviews':reviews,
    }
    return render(request, 'settings/home.html', context)