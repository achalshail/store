from rest_framework import serializers
from . import models

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"
        read_only_fields=['pimage']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['pimage']