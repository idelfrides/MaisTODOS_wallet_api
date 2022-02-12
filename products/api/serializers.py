from dataclasses import fields
from django.urls import clear_script_prefix
from rest_framework.serializers import ModelSerializer
from products.models import Products

class ProductSerializer(ModelSerializer):

    class Meta:
        model = Products
        fields = ['product_type', 'value', 'quantity']
