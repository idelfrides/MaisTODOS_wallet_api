# Generated by Django 2.2.5 on 2022-02-11 19:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('redeVaregista', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redevaregista',
            name='sold_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Data de venda'),
            preserve_default=False,
        ),
    ]