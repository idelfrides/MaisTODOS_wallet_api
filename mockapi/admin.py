from django.contrib import admin
from .models import MockApiResponse


class MockApiModelAdmin(admin.ModelAdmin):

    list_display = ['document', 'cashback', 'id_legacy', 'createdAt']
    list_display_link = ['document']
    list_filter = ['document', 'cashback', 'createdAt']
    list_editable = ['cashback']

    class Meta:
        model = MockApiResponse


admin.site.register(
    MockApiResponse,
    MockApiModelAdmin
)
