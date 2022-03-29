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
    

    def __str__(self):
        return self.name
