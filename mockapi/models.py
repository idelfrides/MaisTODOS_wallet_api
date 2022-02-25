from email import message
from django.db import models

# Create your models here.

class MockApiResponse(models.Model):

    document = models.CharField(
        verbose_name='CPF do cliente',
        blank=False, null=False,
        max_length=18
    )

    createdAt = models.DateTimeField(verbose_name='Data de criação do cashback')

    cashback = models.IntegerField()

    message = models.CharField(max_length=800)

    id_legacy = models.CharField(
        max_length=10,
        help_text='Id do registro na API mock'
    )


    def __str__(self):
        return self.document
