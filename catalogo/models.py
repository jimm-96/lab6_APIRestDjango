from django.db import models


class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    categoria = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Chef(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    anios_experiencia = models.IntegerField()

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
