from rest_framework import serializers
from .models import Product, Brand
from django.db.models.aggregates import Avg



# Serializer
# will Show Format of Data

class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        
        
        
class ProductSerializer(serializers.ModelSerializer):
    # calc fields
    
    ### show all brand detail
    # brand = BrandListSerializer()
    
    ### show only __str__ of brand model 
    brand = serializers.StringRelatedField()
    
    
    avg_rate = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()
    price_with_tax = serializers.SerializerMethodField()
    
    
    
    class Meta:
        model = Product
        fields = '__all__'
        
        
        
    def get_price_with_tax(self, product:Product):
        return product.price*1.5

    def get_reviews_count(self, product:Product):
        reviews_count = product.review_product.all().count()
        return reviews_count
        
    def get_avg_rate(self, product):
        avg = product.review_product.aggregate(rate_avg=Avg('rate'))
        
        if not avg['rate_avg']:
            return 0
        return avg['rate_avg']
        
        

        
class BrandDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(source='product_brand', many=True)
    class Meta:
        model = Brand
        fields = '__all__'