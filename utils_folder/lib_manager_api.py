

import uuid
from customer.models import Customer
from products.models import Products



DISCOUNT = {
    'DIAMANTE': 5,
    'OURO': 3
}


def customer_validation(cpf):

    try:
        customer = Customer.objects.get(cpf=cpf)
        result_ = customer.id
    except Exception as err:
        result_ = f'INFORMED CUSTOMER/CPF -> {cpf} DO NOT EXISTS.'
        print(result_)
        print(f'\n\n API RETURNED:  -> {err}')

    return result_


def product_validation(request_data):

    products_list = []
    type_value_product_list = []
    type_value_dict = {}
    result_code = 200

    all_product_code = request_data.get('product')

    for prod_dict in all_product_code:
        product_code = prod_dict.get('productCode', {})

        try:
            product = Products.objects.get(productCode=product_code)
            result_ = 200
        except Exception as err:
            result_ = f'PRODUCT CODE -> {product_code} DO NOT EXISTS.'
            print(result_)
            print(f'\n\n API RETURNED:  -> {err}')

        if result_ == 200:
            products_list.append(product.id)
            type_value_dict[str(product.product_type)] = product.value
            type_value_product_list.append(type_value_dict)
        else:
            products_list.append(result_)
            result_code = 404
            break

    return result_code, products_list, type_value_product_list


def calculate_discount(type_value_product_list):
    total_discount_value = 0

    for product in type_value_product_list:
        for key, prod_value in product.items():

            discount = DISCOUNT.get(key, 0)
            discount_value  =  (float(prod_value) * (discount/100))

            total_discount_value += discount_value

    return total_discount_value
