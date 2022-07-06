from django.db import models

class personal(models.Model):
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.first_name