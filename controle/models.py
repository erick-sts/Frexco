import datetime

from django.db import models

# Create your models here.

class Usuarios(models.Model):
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100, blank=True)
    nascimento = models.DateField()
