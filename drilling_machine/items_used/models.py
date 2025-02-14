from django.db import models
from inventory.models import InventoryItem  # Import the InventoryItem model

class ItemsUsed(models.Model):
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)  # Link to inventory item
    quantity_used = models.PositiveIntegerField()  # The quantity of the item used
    date_of_use = models.DateField()  # The date when the item is use
    person_responsible = models.CharField(max_length=100, blank=True, null=True)  # New field for person responsible
    description = models.CharField(max_length=300, blank=True, null=True)   # Optional description of the use
    def save(self, *args, **kwargs):
        # Update the inventory quantity when an item is used
        inventory_item = self.inventory_item
        if inventory_item.quantity_in_stock >= self.quantity_used:
            inventory_item.quantity_in_stock -= self.quantity_used  # Deduct the used quantity
            inventory_item.save()  # Save the updated inventory item
        else:
            raise ValueError(f"Not enough stock of {inventory_item.purchased_item.name} to complete the transaction.")
        super().save(*args, **kwargs)
