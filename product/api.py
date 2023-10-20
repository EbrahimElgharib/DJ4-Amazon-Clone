# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from .serializers import ProductSerializer, BrandDetailSerializer, BrandListSerializer

from rest_framework import generics

from .models import Product, Brand



# @api_view(['GET'])
# def product_list_api(request):
#     products = Product.objects.all()[:20]  # list
#     data = ProductSerializer(products, many=True, context={"request":request}).data # json
    
#     return Response({'products':data,})


# @api_view(['GET'])
# def product_detail_api(request, product_id):
#     product = Product.objects.get(id=product_id)  # list
#     data = ProductSerializer(product, context={"request":request}).data # json
    
#     return Response({'product':data,})



class ProductListAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    

class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
   
   
    
    
class BrandListAPI(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
    
    

class BrandDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer