from django.db import models

# Create your models here.

class Triangle(models.Model):
    side1 = models.IntegerField()
    side2 = models.IntegerField()
    side3 = models.IntegerField()

class Meta:
    verbose_name = 'Треугольники'