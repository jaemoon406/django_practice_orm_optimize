from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=15, unique=True)
    parents_category = models.ForeignKey('self', on_delete=models.PROTECT)


class Product(models.Model):
    name = models.CharField(max_length=15, unique=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return Product.name


class Tag(models.Model):
    name = models.CharField(max_length=15, unique=True)
    product = models.ManyToManyField(Product, related_name='tag_products')


class Cart(models.Model):
    user = models.ManyToManyField(User)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='cart_products')
