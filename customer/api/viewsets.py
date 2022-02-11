from rest_framework.viewsets import ModelViewSet
from customer.models import Customer

class CustomerViewSet(ModelViewSet):

    queryset = Customer.objects.all()
    # serializer_class =