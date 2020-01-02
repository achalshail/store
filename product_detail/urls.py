from . import views
from django.urls import path
urlpatterns = [
    path('<int:id>', views.new_product_detail),
    # path('',views.product_detail,name='product_detail'),
]