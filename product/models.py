from django.db import models

class Color(models.Model):
    color = models.CharField(max_length=20)

class Size(models.Model):
    size = models.CharField(max_length=10) 

# class Image(models.Model):
#     image = models.ImageField(upload_to='product_images/') 

# Create your models here.
class Product(models.Model):  
    pid = models.CharField(max_length=20)  
    pname = models.CharField(max_length=100)  
    pprice = models.IntegerField()
    prating = models.IntegerField(default=0)
    pshort_description = models.CharField(max_length=300, default="") 
    plong_description = models.CharField(max_length=2000, default="")
    pmanufacturer = models.CharField(max_length=2000, default="")

    pimage = models.ImageField(null=True, blank=True,upload_to='product_images/')
    pcolor = models.ManyToManyField(Color)
    psize = models.ManyToManyField(Size)
    class Meta:  
        db_table = "products"