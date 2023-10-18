from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company')
    subtitle = models.TextField(max_length=500)
    call_us = models.CharField(max_length=100, null=True, blank=True)
    email_us = models.EmailField(max_length=100, null=True, blank=True)
    address = models.TextField(max_length=500, null=True, blank=True)
    ios_app = models.URLField(max_length=200, null=True, blank=True)
    android_app = models.URLField(max_length=200, null=True, blank=True)
    facebook_link = models.URLField(max_length=200, null=True, blank=True)
    twitter_link = models.URLField(max_length=200, null=True, blank=True)
    youtube_link = models.URLField(max_length=200, null=True, blank=True)
    linkedin_link = models.URLField(max_length=200, null=True, blank=True)
    instagram_link = models.URLField(max_length=200, null=True, blank=True)
    pinterest_link = models.URLField(max_length=200, null=True, blank=True)
    
    # phones = models.
    
    def __str__(self):
        return self.name
    
    
class CompanyPhones(models.Model):
    company = models.ForeignKey(Company, related_name='company_phone', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        return str(self.company) 