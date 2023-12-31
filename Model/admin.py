
from django.contrib import admin
from .models import Invoice, InvoiceDetail

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('date', 'customer_name')  # Customize the fields displayed in the list view
    search_fields = ('customer_name',)        # Add fields to the search functionality

class InvoiceDetailAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'description', 'quantity', 'unit_price', 'price')
    search_fields = ('description', 'invoice__customer_name')  # Search by related fields

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceDetail, InvoiceDetailAdmin)
