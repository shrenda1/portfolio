from django.db import models

class projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=500)