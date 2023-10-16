from django.shortcuts import render


from django.views.generic import ListView, DetailView

from .models import Product, ProductImages, Review, Brand
# Create your views here.


# debug - queryset api tests
def queryset_debug(request):
    # data = Product.objects.all() # all products
    # data = Product.objects.select_related('brand').all() # join with brand table
    data = Product.objects.select_related('brand').all() # 
    
    
    # continued .......................
    
    return render(request, 'product/debug.html', {'data':data})





# product list
class ProductList(ListView):
    model = Product
    paginate_by = 20
    
# product details
class ProductDetail(DetailView):
    model = Product   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(product=self.get_object())   
        context['related_products'] = Product.objects.filter(brand=self.get_object().brand)   
        
        return context          
    
    
class BrandList(ListView):
    model = Brand
    paginate_by = 20


class BrandDetail(ListView):
    model = Product
    template_name = 'product/brand_detail.html'
    
    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        return super().get_queryset().filter(brand=brand)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = Brand.objects.get(slug=self.kwargs['slug'])
        
        return context  