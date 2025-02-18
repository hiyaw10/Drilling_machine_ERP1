from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from decimal import Decimal

class Category(models.Model):
    item_name = models.CharField(max_length=100)

    def __str__(self):
        return self.item_name

# Predefined categories
@receiver(post_migrate)
def create_default_categories(sender, **kwargs):
    categories = [
        'Main Consumables',
        'Lubricants',
        'Service Items',
        'Maintenance Items'
    ]
    for category_name in categories:
        Category.objects.get_or_create(item_name=category_name)


class Item(models.Model):
    BANK_CHOICES = [
        ('CBE', 'Commercial Bank of Ethiopia'),
        ('Abyssinia Bank', 'Abyssinia Bank'),
        ('Oromia Bank', 'Oromia Bank'),
    ]
    
    CATEGORY_CHOICES = [
        ('with', 'With'),
        ('without', 'Without'),
    ]

    ITEM_CATEGORY_CHOICES = [
        ('Main Consumables', 'Main Consumables'),
        ('Lubricants', 'Lubricants'),
        ('Service Items', 'Service Items'),
        ('Maintenance Items', 'Maintenance Items'),
    ]
    
    CATEGORY_NAME_CHOICES = [
        ('Shank', 'Shank'),
        ('Rod', 'Rod'),
        ('Bit', 'Bit'),
        ('Coupling', 'Coupling'),
        ('Liquid consumable', 'Liquid consumable'),
        ('Gas consumable', 'Gas consumable'),
        ('Filter', 'Filter'),
        ('Other', 'Other'),
    ]
    
    FS_number = models.CharField(max_length=100)  # New field for FS number
    Receipt= models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    item_name = models.CharField(max_length=100, choices=CATEGORY_NAME_CHOICES)  # Updated field name
    custom_item_name = models.CharField(max_length=100, blank = True)  # New field for custom name
    item_category = models.CharField(max_length=50, choices=ITEM_CATEGORY_CHOICES)  # Renamed field for clarity
    credit_paid = models.CharField(max_length=100, choices=[('Credit', 'Credit'), ('Paid', 'Paid')])  # New field for payment status
    remark = models.TextField(blank=True, null=True)  # New text field for remarks
    unit_price_before_vat = models.DecimalField(max_digits=10, decimal_places=2)  # Renamed unit price field
    status = models.CharField(max_length=100, choices=[('Finished', 'Finished'), ('Unfinished', 'Unfinished')], blank=True)  # New status field for finished/unfinished
    quantity = models.IntegerField()
    unit = models.CharField(max_length=50, choices=[('Pcs', 'Pcs'), ('Liter', 'Liter'), ('Kg', 'Kg')])
    seller_name = models.CharField(max_length=100, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Total price is nullable
    date_of_purchase = models.DateField()
    date_of_purchase_ethiopian = models.CharField(max_length=50, blank=True)
    serial_number = models.CharField(max_length=100, unique=True, blank=True)
    model = models.CharField(max_length=100, blank=True, null=True)  # Make model optional
    color = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True)
    Transferred_to_bank_name = models.CharField(max_length=30, choices=BANK_CHOICES, blank=True, null=True)
    Transferred_from_bank_name = models.CharField(max_length=30, choices=BANK_CHOICES, blank=True, null=True)
    Transferred_to_account_number = models.CharField(max_length=100, blank=True, null=True)
    Transferred_from_account_number = models.CharField(max_length=100, blank=True, null=True)
    Transferred_to_receiver_name = models.CharField(max_length=100, blank=True, null=True)
    Transferred_from_sender_name = models.CharField(max_length=100, blank=True, null=True)

    def calculate_total_price(self):
        if self.Receipt == 'with':
            return self.unit_price_before_vat * self.quantity * Decimal('1.15')  # Use Decimal here
        else:
            return self.unit_price_before_vat * self.quantity

    def save(self, *args, **kwargs):
        self.total_price = self.calculate_total_price()  # Automatically calculate total price
        super().save(*args, **kwargs)  # Call the parent class's save method to save the object

    def __str__(self):
        return f'{self.item_name} - {self.serial_number}'

    class Meta:
        ordering = ['-date_of_purchase']  # Ensure new purchases are at the top of the report
