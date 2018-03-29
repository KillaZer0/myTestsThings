from django.db import models

class OrderItem(models.Model):
    
    order_id = models.ForeignKey(
        'OrderCard', on_delete = models.CASCADE,
    )
    product_id = models.ForeignKey(
        'Product', on_delete = models.CASCADE,
    )
