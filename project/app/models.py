from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.TextFiled(max_lengyh=250)
    