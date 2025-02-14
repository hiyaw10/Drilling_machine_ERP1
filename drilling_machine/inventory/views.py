from django.shortcuts import render
from .models import InventoryItem

def inventory_list(request):
    # Fetch inventory items with quantity_in_stock > 0
    inventory_items = InventoryItem.objects.filter(quantity_in_stock__gt=0)
    return render(request, 'inventory/inventory_list.html', {'inventory_items': inventory_items})
