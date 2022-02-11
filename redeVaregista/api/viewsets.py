import imp
from rest_framework.viewsets import ModelViewSet
from .serializers import RedeVaregistaSerializer
from redeVaregista.models import RedeVaregista
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class RedeVaregistaViewSet(ModelViewSet):

    queryset = RedeVaregista.objects.all()
    serializer_class = RedeVaregistaSerializer

    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
