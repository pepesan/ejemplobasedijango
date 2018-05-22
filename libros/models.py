from django.db import models
from django.utils import timezone
import datetime


class Libro(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return 'libros:libros_libro_list'
