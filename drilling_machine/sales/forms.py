from django import forms
from .models import Project, SalesRecord

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'company_name', 'agreed_meters']

class SalesRecordForm(forms.ModelForm):
    class Meta:
        model = SalesRecord
        exclude = ['total_hours', 'total_price_with_vat']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'morning_start_time': forms.TimeInput(attrs={'type': 'time'}),
            'morning_end_time': forms.TimeInput(attrs={'type': 'time'}),
            'afternoon_start_time': forms.TimeInput(attrs={'type': 'time'}),
            'afternoon_end_time': forms.TimeInput(attrs={'type': 'time'}),
        }
