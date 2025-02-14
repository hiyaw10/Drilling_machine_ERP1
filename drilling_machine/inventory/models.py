from django.db import models
from purchase.models import Item  # Assuming the model name is PurchasedItem

class InventoryItem(models.Model):
    purchased_item = models.OneToOneField(Item, on_delete=models.CASCADE)  # Link to the purchased item
    quantity_in_stock = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Check if quantity_in_stock is zero, and if so, delete the item
        if self.quantity_in_stock == 0:
            self.delete()  # Delete the inventory item if stock is 0
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.purchased_item.name} - {self.quantity_in_stock} in stock"
    # inventory/models.py
