from django.db.models.signals import post_save
from django.dispatch import receiver
from purchase.models import Item
from .models import InventoryItem

@receiver(post_save, sender=Item)
def create_inventory_item(sender, instance, created, **kwargs):
    if created:
        InventoryItem.objects.create(
            purchased_item=instance,
            quantity_in_stock=instance.quantity
        )
    else:
        inventory_item, _ = InventoryItem.objects.get_or_create(purchased_item=instance)
        inventory_item.quantity_in_stock = instance.quantity
        inventory_item.save()
