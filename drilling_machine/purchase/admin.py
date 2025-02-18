from django.contrib import admin
from .models import Category, Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    # Specify the fields for the admin list display
    list_display = [
        'item_name',                # Renamed field
        'FS_number',
        'Receipt',                
        'serial_number',            # Assuming 'serial_number' exists in Item model
        'item_category',            # Renamed field (ForeignKey to Category)
        'quantity',                 # Assuming 'quantity' exists in Item model
        'unit_price_before_vat',    # Renamed field
        'total_price',              # Assuming 'total_price' exists in Item model
        'date_of_purchase',         # Assuming 'date_of_purchase' exists in Item model
        'status',                   # Added status field               # Added bank_name field
        'remark',                   # Added remark field
        'credit_paid',              # Added credit_paid field
    ]
    
    # Enabling search functionality for item_name and serial_number
    search_fields = ['item_name', 'serial_number', 'fs_number']
    
    # Filtering by item_category, credit_paid, status, and date_of_purchase
    list_filter = ['item_category', 'credit_paid', 'status', 'date_of_purchase']

    # Optional: If item_category is a ForeignKey, use its related field for display
    def item_category(self, obj):
        return obj.item_category.name if obj.item_category else '-'
    item_category.short_description = 'Item Category'


    # Optional: If status is a CharField with choices, display status as readable text
    def status(self, obj):
        return dict(Item.STATUS_CHOICES).get(obj.status, '-')
    status.short_description = 'Status'

# Register the Category model in the admin interface
admin.site.register(Category)
