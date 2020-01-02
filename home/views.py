from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from product.models import Product


# Create your views here.
def home(request): 
   products = Product.objects.all()

   template = loader.get_template('index.html')
   return HttpResponse(template.render({'products':products,"request":request}))