from . import views
from django.urls import path
urlpatterns = [
    
    path('',views.contact,name='contact'),
    path('success/', views.contact_success, name='contact_success'),
]