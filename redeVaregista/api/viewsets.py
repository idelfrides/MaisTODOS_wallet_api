from rest_framework.viewsets import ModelViewSet
from products.models import Products
from customer.models import Customer
from .serializers import RedeVaregistaSerializer
from redeVaregista.models import RedeVaregista
from rest_framework.filters import SearchFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from utils_folder.lib_manager_api import (
    customer_validation,
    product_validation,
    calculate_discount
)
from views import make_request



class RedeVaregistaViewSet(ModelViewSet):

    queryset = RedeVaregista.objects.all()
    serializer_class = RedeVaregistaSerializer

    filter_backends = (SearchFilter, )
    search_fields = ('name', 'sold_at')

    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    @action(methods=['POST', 'OPTIONS'], detail=False)
    def cashback(self, request, *args, **kwarg):

        content_to_request = {}

        cpf = request.data.get('customer', {})['document']

        customer_id = customer_validation(cpf)

        if str(customer_id).isnumeric():
            request.data['customer']  = customer_id
        else:
            return  Response({'Response': customer_id})

        result_code, product_list, type_value_product_list = (
            product_validation(request.data)
        )

        if result_code == 404:
            result = product_list[len(product_list)-1]
            return Response({'Response': result})
        else:
            request.data['product'] = product_list

        result_data = super().create(request, args, kwarg)

        discount_result = calculate_discount(type_value_product_list)

        content_to_request['cpf'] = cpf
        content_to_request['cashback'] = discount_result

        cashback_result = make_request(content_to_request)

        return Response(cashback_result[1])
