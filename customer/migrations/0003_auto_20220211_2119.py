# Generated by Django 2.2.5 on 2022-02-11 21:19

import cpf_field.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_cpf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='document',
        ),
        migrations.AlterField(
            model_name='customer',
            name='cpf',
            field=cpf_field.models.CPFField(max_length=14, verbose_name='CPF do cliente'),
        ),
    ]
