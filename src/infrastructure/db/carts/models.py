from django.db import models
from django.contrib.auth import get_user_model
from src.infrastructure.db.products.models import Product

User = get_user_model()


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='cart_products')
