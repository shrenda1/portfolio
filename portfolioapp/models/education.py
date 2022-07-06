from django.db import models

class education(models.Model):
    education_level = models.CharField(max_length = 100)
    school_name = models.CharField(max_length = 100)
    end_year = models.CharField(max_length = 100)