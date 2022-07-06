from django.db import models

class skills(models.Model):
    skill_name = models.CharField(max_length=500)

    def __str__(self):
        return self.skill_name