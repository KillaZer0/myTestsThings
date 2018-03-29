from django.db import models

class OrderCard(models.Model):
    
    contact_id = models.ForeignKey(
        'Contact', on_delete = models.CASCADE,
    )
    order_date = models.DateField()
    ORDER_STATES = (
        (0, 'Принят в обработку'),
        (1, 'Выполнен'),
    )
    order_state = models.IntegerField(
        choices = ORDER_STATES,
    )
