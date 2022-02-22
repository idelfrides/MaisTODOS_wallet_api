

import uuid
# from customer.models import Customer

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

def customer_validation(request_data):
    import pdb; pdb.set_trace()

    # customers = Customer.objects.all()

    pass


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
