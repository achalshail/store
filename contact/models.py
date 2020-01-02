#this file is not used.
from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=500)


    #just for testing knowledge
    def get_first_name(self):
        return"shyam"