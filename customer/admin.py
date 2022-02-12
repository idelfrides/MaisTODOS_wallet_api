import imp
from django.contrib import admin
from .models import Customer
# Register your models here.

class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'cpf']
    list_display_links = ['name']
    list_filter = ['name']
    list_editable = ['cpf']
    class Meta:
        model = Customer


admin.site.register(
    Customer,
    CustomerModelAdmin
)