
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()


from faker import Faker
import random

from django.contrib.auth.models import User

from product.models import Brand, Product, Review



def seed_brand(n):
    fake = Faker()
    
    for _ in range(n):
        Brand.objects.create(
            name = fake.name(),
            image = f'brands/{random.randint(10,24)}.webp'
        )
    
    print(f"###### seed {n} Brands Successfully ######")



def seed_product(n):
    fake = Faker()
    flags = ['New', 'Sale', 'Feature']
    
    for _ in range(n):
        Product.objects.create(
            name = fake.name(),
            image = f'products/{random.randint(10,24)}.webp',
            flag = flags[random.randint(0,2)],
            price = round(random.uniform(20.99, 199.99),2),
            sku = random.randint(1000, 9999999999),
            subtitle = fake.text(max_nb_chars=250),
            description = fake.text(max_nb_chars=20000),
            quantity = random.randint(0, 30),
            brand = Brand.objects.get(id=random.randint(13, 215)),
        )
    
    print(f"###### seed {n} Products Successfully ######")
    
    
def seed_reviews(n):
    fake = Faker()
    
    for i in range(n):
        Review.objects.create(
            user = User.objects.get(id=1),
            review = fake.text(max_nb_chars=150),
            rate = random.randint(0, 5),
            product = Product.objects.get(id=i+5),
        )
    
    print(f"###### seed {n} Products Successfully ######")

# seed_brand(200)
# seed_reviews(500)