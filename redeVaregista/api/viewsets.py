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
    customer_validation
)
import requests


DISCOUNT = {
    'DIAMANTE': 5,
    'OURO': 3
}


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
            return customer_id

        result_code, product_list, type_value_product_list = (
            self.product_validation(request.data)
        )

        if result_code == 404:
            return product_list[len(product_list)-1]
        else:
            request.data['product'] = product_list

        result_data = super().create(request, args, kwarg)

        discount_result = self.calculate_discount(type_value_product_list)

        content_to_request['cpf'] = cpf
        content_to_request['cashback'] = discount_result

        cashback_result = self.make_request(content_to_request)

        return Response(cashback_result[1])


    def customer_validation(self, cpf):
        customer = Customer.objects.get(cpf=cpf)

        if not customer:
            result_ = 'INFORMED CPF DO NOT EXISTS.'
        else:
            result_ = customer.id

        return result_


    def product_validation(self, request_data):

        products_list = []
        type_value_product_list = []
        type_value_dict = {}
        result_code = 200

        all_product_code = request_data.get('product')

        for prod_dict in all_product_code:
            product_code = prod_dict.get('productCode', {})

            product = Products.objects.get(productCode=product_code)

            if product:
                products_list.append(product.id)
                type_value_dict[str(product.product_type)] = product.value
                type_value_product_list.append(type_value_dict)
            else:
                result_ = f'PRODUCT CODE {product_code} DO NOT EXISTS.'
                products_list.append(result_)
                result_code = 404
                break

        return result_code, products_list, type_value_product_list


    def calculate_discount(self, type_value_product_list):
        total_discount_value = 0

        for product in type_value_product_list:
            for key, prod_value in product.items():

                discount = DISCOUNT.get(key, 0)
                discount_value  =  (float(prod_value) * (discount/100))

                total_discount_value += discount_value

        return total_discount_value


    def make_request(self, request_data):
        url = 'https://5efb30ac80d8170016f7613d.mockapi.io/api/mock/Cashback'

        data_content = {
            'document': request_data['cpf'],
            'cashback': request_data['cashback']
        }

        try:
            payload = requests.post(url, json=data_content)
        except Exception as err:
            print(f'EXCEPTION: {err}')
            payload = requests.post(url, data=data_content)

        if payload.status_code in (200, 201):
            content_payload = payload.json()
        else:
            content_payload = {}

        return payload.status_code, content_payload
