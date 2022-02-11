from rest_framework.viewsets import ModelViewSet
from customer.api.serializers import CustomerSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from customer.models import Customer

class CustomerViewSet(ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    filter_backends = (SearchFilter, )
    search_fields = ('name', 'cpf')

    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )