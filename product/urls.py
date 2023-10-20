from django.urls import path

from .views import ProductDetail, ProductList, BrandList, BrandDetail, queryset_debug
# from .api import product_list_api, product_detail_api
from .api import ProductListAPI, ProductDetailAPI


urlpatterns = [
    path('', ProductList.as_view()),
    path('debug', queryset_debug),

    path('<slug:slug>', ProductDetail.as_view()),
    path('brands/', BrandList.as_view()),
    path('brands/<slug:slug>', BrandDetail.as_view()),
    
    
    # api
    # path('api/list', product_list_api),
    path('api/list', ProductListAPI.as_view()),
    # path('api/list/<int:product_id>', product_detail_api),
    path('api/list/<int:pk>', ProductDetailAPI.as_view()),
]