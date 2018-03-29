from django.db import models

class Product(models.Model):

    name = models.CharField(
        max_length = 255,
    )
    description = models.CharField(
        max_length = 1024,
    )
    price_id = models.ForeignKey(
        'Price', on_delete = models.CASCADE,
    )
    category_id = models.ForeignKey(
        'ProductCategory', on_delete = models.SET_NULL,
        null = True,
    )
