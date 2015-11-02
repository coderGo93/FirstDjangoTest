from django.db import models

# Create your models here.

class Info(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    fechaNacimiento = models.DateField()

