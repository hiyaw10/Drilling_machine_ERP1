from django.db import models

class Contract(models.Model):
    business_name = models.CharField(max_length=255)
    meters_agreed = models.DecimalField(max_digits=10, decimal_places=2)

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)

class BankTransferDetail(models.Model):
    from_account_number = models.CharField(max_length=50)
    from_bank_name = models.CharField(max_length=100)
    from_sender_name = models.CharField(max_length=100)
    to_account_number = models.CharField(max_length=50)
    to_bank_name = models.CharField(max_length=100)
    to_receiver_name = models.CharField(max_length=100)

from django.db import models

class SalesRecord(models.Model):
    fs_number = models.CharField(max_length=50)
    date = models.DateField()
    drilled_meters = models.DecimalField(max_digits=10, decimal_places=2)
    worked_hours = models.DecimalField(max_digits=6, decimal_places=2)
    unit_price_without_vat = models.DecimalField(max_digits=10, decimal_places=2)
    total_price_including_vat = models.DecimalField(max_digits=10, decimal_places=2)
    buyer_name = models.CharField(max_length=100)
    tin_number = models.CharField(max_length=50)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    bank_transfer = models.OneToOneField('BankTransferDetail', on_delete=models.CASCADE)