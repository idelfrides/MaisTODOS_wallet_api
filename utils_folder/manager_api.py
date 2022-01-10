import uuid

class ManagerWalletAPI(object):

    def __init__(self):
        pass

    def generate_uuid(self, parts=''):
        # import pdb; pdb.set_trace()

        assert str(parts).isnumeric, 'PARAMETER parts MUST BE A NUMBER'

        the_uuid = uuid.uuid4()
        code_help = str(the_uuid).split('-')
        uuid_code = (
            code_help[0][:parts] + code_help[1][:parts] + code_help[2][:parts] + code_help[3][:parts] + code_help[4][:parts]
        )

        return 'C:'+uuid_code


    def customer_validation(self):
        pass

    def product_validation(self):
        pass
    