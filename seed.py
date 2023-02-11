from product.models import Product
from django.contrib.auth.models import User
import json

file = open('products.json', 'r')
products = json.load(file)

for product in products:
    if not Product.objects.filter(name=product['name']).exists():
        Product.objects.create(
            name=product['name'],
            price=product['price'],
            imageURL=product['image'],
            score=product['score'],
        )

file.close()

if not User.objects.filter(username='client').exists():
    user = User.objects.create(
        username='client',
        email='client@example.com',
    )
    user.set_password('client')
    user.save()
