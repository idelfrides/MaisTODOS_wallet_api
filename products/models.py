from django.db import models

# Create your models here.

PRODUCT_CHOICE = [
    ('DIAMANTE', 'Diamante'),
    ('OURO', 'Ouro'),
]

'''
discontos :

diamante: 3%
ouro: 2%
'''


class Products(models.Model):
    product_type = models.CharField(
        verbose_name='Tipo do produto', choices=PRODUCT_CHOICE
    )

    value = models.IntegerField(
        verbose_name='Valor do produto', blank=False, null=False)

    quantity = models.IntegerField(
        verbose_name='Quantidade de produto', blank=False, null=False)


    def __str__(self):
        return self.product_type