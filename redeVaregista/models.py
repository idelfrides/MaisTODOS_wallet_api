from django.db import models

class RedeVaregista(models.Model):
    name = models.CharField(verbose_name='Nome do varegista', max_length=300)
    total = models.IntegerField(verbose_name='Total de registros')
    sold_at = models.DateTimeField(
        verbose_name='Data de venda', null=False)

    # customer = models.ManyToManyField()
    # product = models.ManyToManyField()

    def __str__(self):
        return self.name