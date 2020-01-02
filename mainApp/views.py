from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import csv
from reportlab.pdfgen import canvas
from .models import Entry

def layout(request):  
   template = loader.get_template('layout.html')
   return HttpResponse(template.render({"request":request}))
#image pathaunalai test gareko 



def get_image(request):
   png_image = open("D:/study/broadway/lastproject/store/mainApp/static/images/loc.png","rb").read()
   return HttpResponse(png_image, content_type="image/png")

def get_csv(request):
   number_of_births = [146,184,235,200,226,251,299,273,281,304,203]
   response = HttpResponse(content_type='text/csv')
   response['Content-Disposition'] = 'attachment; filename=births.csv'
   writer = csv.writer(response)
   writer.writerow(['Year', 'Total child birth'])
   for (year, num) in zip(range(1995, 2006), number_of_births):
       writer.writerow([year, num])

   return response

def get_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'
    p = canvas.Canvas(response)
    p.drawString(10, 10, "Hello world.")
    p.showPage()
    p.save()
    return response


# news feed ko lagi
def entry(request, id):
   my_entry = Entry.objects.get(id = id)
   text = '<strong>User :</strong> {} <p>'.format(my_entry.first_description) + '</p>'
   text += '<strong>Comment :</strong> %s <p>'.format(my_entry.second_description) + '</p>'
   return HttpResponse(text)