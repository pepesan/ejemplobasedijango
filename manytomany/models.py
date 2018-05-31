from django.db import models

class Course(models.Model):
    name=models.CharField(max_length=100)
    tags = models.ManyToManyField('Tag', db_table='course_tag',
                                  related_name='courses', blank=True)

class Tag(models.Model):
    name = models.CharField(max_length=100)


class Autor(models.Model):
    name=models.CharField(max_length=100)
    libros = models.ManyToManyField('Libro', db_table='libro_autor',
                                  related_name='autores', blank=True)

class Libro(models.Model):
    name = models.CharField(max_length=100)