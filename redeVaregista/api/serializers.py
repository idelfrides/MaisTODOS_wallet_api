from rest_framework.serializers import ModelSerializer
from redeVaregista.models import RedeVaregista

class RedeVaregistaSerializer(ModelSerializer):

    class Meta:
        model = RedeVaregista
        fields = ['id', 'name', 'sold_at', 'total', 'customer', 'product']
        