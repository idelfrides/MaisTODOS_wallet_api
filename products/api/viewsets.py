from rest_framework.viewsets import ModelViewSet
from products.api.serializers import ProductSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from products.models import Products

class ProductViewSet(ModelViewSet):

    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    filter_backends = (SearchFilter, )
    search_fields = ('name', 'value', 'quantity')

    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
