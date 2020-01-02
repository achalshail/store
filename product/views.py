from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from .models import Product
from rest_framework import response
from rest_framework.decorators import action
from rest_framework import parsers

# Create your views here.
class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer

    @action(
        detail=True,
        methods=['PUT'],
        serializer_class=serializers.ProductImageSerializer,
        parser_classes=[parsers.MultiPartParser],
    )
    def pic(self, request, pk):
        obj = self.get_object()
        serializer = self.serializer_class(obj, data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors,
                                 status.HTTP_400_BAD_REQUEST)