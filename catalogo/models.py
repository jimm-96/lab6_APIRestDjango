from django.db import models

# Create your models here.


class Chef(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    anios_experiencia = models.IntegerField()
