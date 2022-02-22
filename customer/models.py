from enum import unique
from os import name
from django.db import models
from cpf_field.models import CPFField


class Customer(models.Model):

    cpf = CPFField('CPF do cliente')
    name = models.CharField(
        verbose_name='Nome do cliente',
        max_length=300,
    )

    def __str__(self):
        return self.name
