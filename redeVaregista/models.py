import uuid
from django.db import models
from customer.models import Customer
from products.models import Products

class RedeVaregista(models.Model):

    name = models.CharField(
        verbose_name='Nome do varegista',
        max_length=300
    )
    total =models.IntegerField(
        verbose_name='Total de registros'
    )
    sold_at = models.DateTimeField(
        verbose_name='Data de venda',
        null=False
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        blank=False, null=False
    )

    product = models.ManyToManyField(
        Products
    )



    # TODO: make all content of a customer to appear  when call get  redevaregista

    def __str__(self):
        return self.name

'''
class CreatedUUID(models.Model):

    id = models.UUIDField(
        verbose_name='Codigo Unico',
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    code_help = id.split('-')
    code = code_help[0][:2] + code_help[1][:2] + code_help[2][:2] + code_help[3][:2] + code_help[4][:2]
'''