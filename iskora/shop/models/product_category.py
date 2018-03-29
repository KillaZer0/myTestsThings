from django.db import models

class ProductCategory(models.Model):
    
    name = models.CharField(
        max_length = 255,
    )
    root = models.ForeignKey(
        'self',
        on_delete = models.CASCADE,
        null = True,
        default = 0,
    )

    def __str__(self):
        
	    return self.name
