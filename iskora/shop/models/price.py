from django.db import models

class Price(models.Model):
    
    amount = models.BigIntegerField()
    digits = models.IntegerField()
    currency = models.CharField(
        max_length = 4,
    )
