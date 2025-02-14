from django.db import models
from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from decimal import Decimal

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

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
        Category.objects.get_or_create(name=category_name)


class Item(models.Model):
    CATEGORY_CHOICES = [
        ('with', 'With'),
        ('without', 'Without'),
    ]

   
    CLASS_CHOICES = [
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

    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)  # "With" or "Without"
    item_class = models.CharField(max_length=50, choices=CLASS_CHOICES, null=True, blank=True)
    name = models.CharField(max_length=100, choices=CATEGORY_NAME_CHOICES)  # Predefined Name options
    custom_name = models.CharField(max_length=100, blank=True, null=True)  # Make custom_name optional  # Custom name is nullable
    serial_number = models.CharField(max_length=100, unique=True)
    model = models.CharField(max_length=100, blank=True, null=True)  # Make model optional
    color = models.CharField(max_length=100, blank=True, null=True) 
    brand = models.CharField(max_length=50)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=50, choices=[('Pcs', 'Pcs'), ('Liter', 'Liter'), ('Kg', 'Kg')])
    seller_name = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Total price is nullable
    date_of_purchase = models.DateField()
    date_of_purchase_ethiopian = models.CharField(max_length=50)

    def calculate_total_price(self):
        if self.category == 'with':
            return self.unit_price * self.quantity * Decimal('1.15')  # Use Decimal here
        else:
            return self.unit_price * self.quantity
    def save(self, *args, **kwargs):
        self.total_price = self.calculate_total_price()  # Automatically calculate total price
        super().save(*args, **kwargs)  # Call the parent class's save method to save the object

    def __str__(self):
        return f'{self.name} - {self.serial_number}'
    
    
    
    