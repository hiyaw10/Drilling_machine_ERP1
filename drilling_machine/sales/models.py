from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError
from datetime import timedelta

class Project(models.Model):
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    agreed_meters = models.IntegerField()

    def __str__(self):
        return self.name

class SalesRecord(models.Model):
    fs_number = models.CharField(max_length=100, unique=True)
    date = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="sales")
    drilled_meters = models.IntegerField()
    
    # Time fields
    morning_start_time = models.TimeField()
    morning_end_time = models.TimeField()
    afternoon_start_time = models.TimeField()
    afternoon_end_time = models.TimeField()

    # Pricing
    unit_price_without_vat = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Buyer info
    buyer_name = models.CharField(max_length=255)
    tin_number = models.CharField(max_length=100)

    # Bank Transfer Details
    bank_transferred_from_account_number = models.CharField(max_length=50)
    bank_transferred_from_name = models.CharField(max_length=100)
    bank_transferred_from_account_sender_name = models.CharField(max_length=255)
    bank_transferred_to_account_number = models.CharField(max_length=50)
    bank_transferred_to_name = models.CharField(max_length=100)
    bank_transferred_to_account_receiver_name = models.CharField(max_length=255)

    @property
    def total_hours(self):
        """Calculate total working hours"""
        morning_hours = self._calculate_hours(self.morning_start_time, self.morning_end_time)
        afternoon_hours = self._calculate_hours(self.afternoon_start_time, self.afternoon_end_time)
        return morning_hours + afternoon_hours

    @property
    def total_price_with_vat(self):
        """Calculate total price with VAT (15%)"""
        return self.unit_price_without_vat * self.drilled_meters * 1.15

    def _calculate_hours(self, start_time, end_time):
        """Helper function to calculate time differences in hours"""
        start = timedelta(hours=start_time.hour, minutes=start_time.minute)
        end = timedelta(hours=end_time.hour, minutes=end_time.minute)
        if end < start:
            raise ValidationError("End time cannot be before start time.")
        return (end - start).total_seconds() / 3600

    def save(self, *args, **kwargs):
        """Ensure total hours calculation before saving"""
        self.total_hours  # Trigger validation
        super().save(*args, **kwargs)

    def __str__(self):
        return f"FS#{self.fs_number} - {self.project.name}"
