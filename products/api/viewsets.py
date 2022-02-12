from rest_framework.viewsets import ModelViewSet
from products.api.serializers import ProductSerializer
from products.models import Products

class ProductViewSet(ModelViewSet):

    queryset = Products.objects.all()
    serializer_class = ProductSerializer
