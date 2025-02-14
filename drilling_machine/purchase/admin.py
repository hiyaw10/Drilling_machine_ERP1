from django.contrib import admin
from .models import Category, Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'serial_number', 'category', 'quantity', 'unit_price', 'total_price', 'date_of_purchase', 'item_class']
    search_fields = ['name', 'serial_number']
    list_filter = ['item_class', 'date_of_purchase']


