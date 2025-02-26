from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Contract, Project, SalesRecord, BankTransferDetail

admin.site.register(Contract)
admin.site.register(Project)
admin.site.register(SalesRecord)
admin.site.register(BankTransferDetail)

