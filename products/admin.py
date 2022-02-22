from django.contrib import admin
from .models import Products
# Register your models here.

class ProductModelAdmin(admin.ModelAdmin):

    list_display = ['product_type', 'value', 'quantity', 'productCode']
    list_display_links = ['product_type']
    list_filter = ['quantity', 'value']
    list_editable = ['value', 'quantity']

    class Meta:
        model = Products


admin.site.register(
    Products,
    ProductModelAdmin
)
