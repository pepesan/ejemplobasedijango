from django.db import models

class Course(models.Model):
    name=models.CharField(max_length=100)
    tags = models.ManyToManyField('Tag', db_table='course_tag',
                                  related_name='courses', blank=True)

class Tag(models.Model):
    name = models.CharField(max_length=100)
