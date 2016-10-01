from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Departamento(models.Model):
	Id_departamento = models.CharField(max_length=10, primary_key=True)
	nombre = models.CharField(max_length=50)
	Estado = models.CharField(max_length=10)

