from rest_framework import serializers
from . import models

class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Checkout
        fields = "__all__"