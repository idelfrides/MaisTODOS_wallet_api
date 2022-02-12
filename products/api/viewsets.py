from rest_framework.viewsets import ModelViewSet
from products.models import Products

class ProductViewSet(ModelViewSet):

    queryset = Products.objects.all()
    # serializer_class =
