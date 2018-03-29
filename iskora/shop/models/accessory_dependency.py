from django.db import models

class AccessoryDependency(models.Model):
    
    accessory = models.ForeignKey(
        'Product', on_delete = models.CASCADE,
        related_name = 'accessory'
    )
    accessory_for = models.ForeignKey(
        'Product', on_delete = models.CASCADE,
        related_name = 'accessory_for'
    )
