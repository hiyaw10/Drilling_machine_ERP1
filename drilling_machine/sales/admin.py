from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Project, SalesRecord

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'company_name', 'agreed_meters')

@admin.register(SalesRecord)
class SalesRecordAdmin(admin.ModelAdmin):
    list_display = ('fs_number', 'date', 'project', 'drilled_meters', 'total_hours', 'total_price_with_vat')
    readonly_fields = ('total_hours', 'total_price_with_vat')  # Ensure these are not editable
