from django.urls import path
from . import views
from . import feeds
from django.conf.urls import *


urlpatterns = [
    path('', views.layout),
    path('get_png_image/', views.get_image),
    path('get_csv/', views.get_csv),
    path('get_pdf/', views.get_pdf),
    path('latest/feed/', feeds.LatestEntries()),
    url(r'^get_entry/(?P<id>[0-9]+)/', views.entry, name = 'entry'),
]