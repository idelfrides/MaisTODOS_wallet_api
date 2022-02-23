

import uuid
from customer.models import Customer

def generate_uuid(parts=''):
    # import pdb; pdb.set_trace()

    assert str(parts).isnumeric, 'PARAMETER parts MUST BE A NUMBER'

    the_uuid = uuid.uuid4()
    # code_help = str(the_uuid).split('-')
    # uuid_code = (
    #     code_help[0][:parts] + code_help[1][:parts] + code_help[2][:parts] + code_help[3][:parts] + code_help[4][:parts]
    # )

    return 'C:' + str(the_uuid)
    # return 'C:' + uuid_code


'''
def generate_product_code():
    import pdb; pdb.set_trace()

    # hd_obj = HoldData()

    # assert eric, 'PARAMETER parts MUST BE A NUMBER'

    n = product.id
    # order_number = hd_obj.get_hold_value()
    order_number += 1

    code = f'Product:{order_number}'

    # hd_obj.set_hold_value(order_number)

    return code

'''


def customer_validation(cpf):

    try:
        customer = Customer.objects.get(cpf=cpf)
        result_ = customer.id
    except Exception as err:
        result_ = f'INFORMED CUSTOMER/CPF -> {cpf} DO NOT EXISTS.'
        print(result_)
        print(f'\n\n API RETURNED:  -> {err}')

    return result_


def product_validation():
    pass


class HoldData(object):

    def __init__(self, value):
        # pass
        self.__hold_value = value


    # GETTER
    def get_hold_value(self):
        return self.__hold_value


    # SETTER
    def set_hold_value(self, in_value):
        self.__hold_value = in_value
