from django.db import models

# Create your models here.


class Entry(models.Model):
    first_description = models.CharField(max_length=100)
    second_description = models.CharField(max_length=100)