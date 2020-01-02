from django.shortcuts import render
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from product.models import Product

# Create your views here.
def new_product_detail(request, id):
   print("id", id) 
   product = Product.objects.get(id=id)
   colors = []
   for color_obj in product.pcolor.all():
      colors.append(color_obj.color)

   sizes = []
   for size_obj in product.psize.all():
      sizes.append(size_obj.size)

   print(sizes)

   print(product.pimage)
   template = loader.get_template('product_detail.html')
   return HttpResponse(template.render({"sizes":sizes,"colors":colors,"product":product,"request":request}))