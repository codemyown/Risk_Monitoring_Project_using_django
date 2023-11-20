# dashboard/models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])
    risky_behavior = models.BooleanField(default=False)

    def __str__(self):
        return self.name
