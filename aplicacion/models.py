from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Buzos(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    talle = models.CharField(max_length=50)
    precio = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    
    
    
    def __str__(self) :
        return f"{self.nombre} / Color: ({self.color}) / Talle: ({self.talle})"


class Remeras(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    talle = models.CharField(max_length=50)
    precio = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    
    
    def __str__(self) :
        return f"{self.nombre} / Color: ({self.color}) / Talle: ({self.talle})"


class Cargos(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    talle = models.CharField(max_length=50)
    precio = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    
    def __str__(self) :
        return f"{self.nombre} / Color: ({self.color}) / Talle: ({self.talle})"


class Bermudas(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    talle = models.CharField(max_length=50)
    precio = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    
    def __str__(self) :
        return f"{self.nombre} / Color: ({self.color}) / Talle: ({self.talle})"



class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.user} [{self.imagen}]"

