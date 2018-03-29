from django.db import models

class Contact(models.Model):
    
    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,
    )
    phone_number = models.CharField(
        max_length=20,
    )
    email = models.EmailField()

    def __str__(self):
        
	    return ' '.join([
            self.phone_number,
            self.first_name,
            self.last_name,
        ])
