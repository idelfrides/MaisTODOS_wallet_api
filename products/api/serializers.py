from rest_framework.serializers import ModelSerializer
from products.models import Products

class ProductSerializer(ModelSerializer):

    class Meta:
        model = Products
        fields = ['id', 'product_type', 'value', 'quantity']
