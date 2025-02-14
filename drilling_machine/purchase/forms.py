
from django import forms
from .models import Item, Category
from decimal import Decimal
from django.forms.widgets import DateInput, SelectDateWidget

class ReportForm(forms.Form):
    
    start_date = forms.DateField(
        widget=forms.SelectDateWidget(years=range(2025, 2040)),
        required=True
    )
    end_date = forms.DateField(
        widget=forms.SelectDateWidget(years=range(2028, 2040)),
        required=True
    )
    item_class = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False
    )
        
        
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'category', 'name', 'custom_name', 'item_class', 'serial_number', 
            'model', 'color', 'brand', 'quantity', 'unit', 'seller_name', 
            'unit_price', 'date_of_purchase', 'date_of_purchase_ethiopian'
        ]
    
    custom_name = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'style': 'display:-;'}))


    # Additional Fields
    serial_number = forms.CharField(required=False, max_length=100)
    model = forms.CharField(required=False, max_length=100)
    color = forms.CharField(required=False, max_length=100)
    brand = forms.CharField(required=False, max_length=100)
    date_of_purchase = forms.DateField(
        widget=forms.TextInput(attrs={'class': 'datepicker', 'placeholder': 'Select Date'})
    )
    total_price = forms.DecimalField(
        max_digits=20, 
        decimal_places=2, 
        required=False, 
        disabled=True
    )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        custom_name = cleaned_data.get('custom_name')

        if name == 'Other' and not custom_name:
            raise forms.ValidationError("Please provide a custom name if 'Other' is selected.")

        return cleaned_data
      
