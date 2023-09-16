from django.shortcuts import render


from django.views.generic import ListView, DetailView

from .models import Product, ProductImages, Review, Brand
# Create your views here.


# product list
class ProductList(ListView):
    model = Product
    
# product details
class ProductDetail(DetailView):
    model = Product