from django.db import models


PRODUCT_CHOICE = [
    ('DIAMANTE', 'Diamante'),
    ('OURO', 'Ouro'),
]


'''
-----------------
Discontos:
-----------------
Diamante: 5%
Ouro: 3%
'''

class Products(models.Model):

    product_type = models.CharField(
        verbose_name='Tipo do produto',
        choices=PRODUCT_CHOICE,
        max_length=150
    )

    value = models.DecimalField(
        verbose_name='Valor do produto',
        blank=False,
        null=False,
        decimal_places=2,
        max_digits=7
    )

    quantity = models.IntegerField(
        verbose_name='Quantidade de produto',
        blank=False,
        null=False
    )

    productCode = models.CharField(
        verbose_name='Código do produto',
        max_length=150,
        help_text='Códico do produto deve ser único',
        unique=True
    )


    def __str__(self):
        return self.product_type
