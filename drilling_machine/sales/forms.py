from django import forms
from .models import Contract, Project, SalesRecord, BankTransferDetail

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['business_name', 'meters_agreed']
        widgets = {
            'business_name': forms.TextInput(attrs={'class': 'form-control'}),
            'meters_agreed': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'contract']
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contract': forms.Select(attrs={'class': 'form-control'}),
        }

class BankTransferForm(forms.ModelForm):
    class Meta:
        model = BankTransferDetail
        fields = [
            'from_account_number', 'from_bank_name', 'from_sender_name',
            'to_account_number', 'to_bank_name', 'to_receiver_name'
        ]
        widgets = {
            'from_account_number': forms.TextInput(attrs={'class': 'form-control'}),
            'from_bank_name': forms.TextInput(attrs={'class': 'form-control'}),
            'from_sender_name': forms.TextInput(attrs={'class': 'form-control'}),
            'to_account_number': forms.TextInput(attrs={'class': 'form-control'}),
            'to_bank_name': forms.TextInput(attrs={'class': 'form-control'}),
            'to_receiver_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SalesRecordForm(forms.ModelForm):
    class Meta:
        model = SalesRecord
        fields = [
            'fs_number', 'date', 'drilled_meters', 'worked_hours',
            'unit_price_without_vat', 'total_price_including_vat',
            'buyer_name', 'tin_number', 'project', 'bank_transfer'
        ]
        widgets = {
            'fs_number': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'drilled_meters': forms.NumberInput(attrs={'class': 'form-control'}),
            'worked_hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit_price_without_vat': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_price_including_vat': forms.NumberInput(attrs={'class': 'form-control'}),
            'buyer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'tin_number': forms.TextInput(attrs={'class': 'form-control'}),
            'project': forms.Select(attrs={'class': 'form-control'}),
            'bank_transfer': forms.Select(attrs={'class': 'form-control'}),
        }