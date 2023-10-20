from rest_framework import serializers

from django.db.models.aggregates import Avg

from .models import Product, Brand, Review

# Serializer
# will Show Format of Data

class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        
        
class ReviewsSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Review
        fields = '__all__' 
        
        
class ProductSerializer(serializers.ModelSerializer):
    # calc fields
    
    ### show all brand detail
    # brand = BrandListSerializer()
    reviews = ReviewsSerializer(source='review_product', many=True)
    
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
    reviews = ReviewsSerializer(source='review_product', many=True)
    
    products = ProductSerializer(source='product_brand', many=True)
    class Meta:
        model = Brand
        fields = '__all__'
        
        
