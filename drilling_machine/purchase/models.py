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

def upload_to_receipts(instance, filename):
    return f"receipts/{instance.serial_number}/{filename}"

def upload_to_bank_transfers(instance, filename):
    return f"bank_transfers/{instance.serial_number}/{filename}"
class Item(models.Model):
   
    BANK_CHOICES = [
    ('CBE', 'Commercial Bank of Ethiopia'),
    ('Awash Bank', 'Awash International Bank'),
    ('Dashen Bank', 'Dashen Bank S.C.'),
    ('Bank of Abyssinia', 'Bank of Abyssinia S.C.'),
    ('Wegagen Bank', 'Wegagen Bank S.C.'),
    ('Nib International Bank', 'Nib International Bank S.C.'),
    ('Hibret Bank', 'Hibret Bank S.C.'),
    ('Oromia Bank', 'Oromia Bank S.C.'),
    ('Cooperative Bank of Oromia', 'Cooperative Bank of Oromia'),
    ('Berhan Bank', 'Berhan International Bank S.C.'),
    ('Bunna Bank', 'Bunna International Bank S.C.'),
    ('Zemen Bank', 'Zemen Bank S.C.'),
    ('Enat Bank', 'Enat Bank S.C.'),
    ('Global Bank Ethiopia', 'Global Bank Ethiopia S.C.'),
    ('Addis International Bank', 'Addis International Bank S.C.'),
    ('Abay Bank', 'Abay Bank S.C.'),
    ('Shabelle Bank', 'Shabelle Bank S.C.'),
    ('ZamZam Bank', 'ZamZam Bank S.C.'),
    ('Goh Betoch Bank', 'Goh Betoch Bank S.C.'),
    ('Ahadu Bank', 'Ahadu Bank S.C.'),
    ('Hijra Bank', 'Hijra Bank S.C.'),
    ('Tsehay Bank', 'Tsehay Bank S.C.'),
    ('Siinqee Bank', 'Siinqee Bank S.C.'),
    ('Tsedey Bank', 'Tsedey Bank S.C.'),
    ('Gadaa Bank', 'Gadaa Bank S.C.'),
    ('Amhara Bank', 'Amhara Bank S.C.'),
    ('Rammis Bank', 'Rammis Bank S.C.'),
    ('Siket Bank', 'Siket Bank S.C.'),
    ('Sidama Bank', 'Sidama Bank S.C.'),
    ('Omo Bank', 'Omo Bank S.C.'),
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
    payment_type = models.CharField(max_length=100, choices=[('Credit', 'Credit'), ('Paid', 'Paid in Full')]) 
    payment_transaction_type = models.CharField(max_length=100, choices=[('Bank Transfer', 'Bank Transfer'), ('Cash', 'Cash')], blank = True, null = True) # New field for payment status
    remark = models.TextField(blank=True, null=True)  # New text field for remarks
    unit_price_before_vat = models.DecimalField(max_digits=10, decimal_places=2)  # Renamed unit price field
    status = models.CharField(max_length=100, choices=[('Finished', 'Finished'), ('Unfinished', 'Unfinished')], blank=True)  # New status field for finished/unfinished
    quantity = models.IntegerField()
    unit = models.CharField(max_length=50, choices=[('Pcs', 'Pcs'), ('Liter', 'Liter'), ('Kg', 'Kg')])
    seller_name = models.CharField(max_length=100, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Total price is nullable
    date_of_purchase = models.DateField()
    receipt_status = models.CharField(max_length=50, choices=[('Taken', 'Taken'),('Not Taken', 'Not Taken')], blank = True, null = True)
    date_of_bank_transfer = models.DateField(null=True, blank=True)
    serial_number = models.CharField(max_length=100, blank=True, unique = True)
    item_destination = models.CharField(max_length=50, choices=[('Item Taken', 'Item Taken'),('Item Not Taken', 'Item Not Taken')])
    model = models.CharField(max_length=100, blank=True, null=True)  # Make model optional
    color = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True)
    Transferred_to_bank_name = models.CharField(max_length=30, choices=BANK_CHOICES, blank=True, null=True)
    Transferred_from_bank_name = models.CharField(max_length=30, choices=BANK_CHOICES, blank=True, null=True)
    Transferred_to_account_number = models.CharField(max_length=100, blank=True, null=True)
    Transferred_from_account_number = models.CharField(max_length=100, blank=True, null=True)
    Transferred_to_receiver_name = models.CharField(max_length=100, blank=True, null=True)
    Transferred_from_sender_name = models.CharField(max_length=100, blank=True, null=True)
    USD_rate = models.DecimalField(max_digits=10, decimal_places=2, null =True, blank=True) 
    total_price_usd = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    receipt_file = models.FileField(upload_to='uploads/receipts/', blank=True, null=True)
    bank_transfer_file = models.FileField(upload_to='uploads/', blank=True, null=True)
    
    def calculate_total_price(self):
        if self.Receipt == 'with':
            return self.unit_price_before_vat * self.quantity * Decimal('1.15')  # Use Decimal here
        else:
            return self.unit_price_before_vat * self.quantity

    def save(self, *args, **kwargs):
        self.total_price = self.calculate_total_price()  # Automatically calculate total price
        if self.USD_rate:
            self.total_price_usd = self.total_price / self.USD_rate 
        super().save(*args, **kwargs)  # Call the parent class's save method to save the object

    def __str__(self):
        return f'{self.item_name} - {self.serial_number}'

    class Meta:
        ordering = ['-date_of_purchase']  # Ensure new purchases are at the top of the report
