"""wallet_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework import routers
from redeVaregista.api.viewsets import RedeVaregistaViewSet
from customer.api.viewsets import CustomerViewSet
from products.api.viewsets import ProductViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()

router.register(
    'wallet/api/cashback', RedeVaregistaViewSet, base_name='RedeVaregista')
router.register('wallet/api/customer', CustomerViewSet)
router.register('wallet/api/product', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token)
]
