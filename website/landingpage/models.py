from django.db import models

# Create your models here.

class Exp(models.Model):
    username = models.CharField(max_length=32)
    method = models.CharField(max_length=2)
    date = models.DateField()
    task = models.CharField(max_length=32)
    hours = models.DecimalField(max_digits=6, decimal_places=1)
    remarks = models.CharField(max_length=64)

    def __str__(self):
        return self.username