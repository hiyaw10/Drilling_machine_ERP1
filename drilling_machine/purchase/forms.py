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
        widget=forms.SelectDateWidget(years=range(2025, 2040)),
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
            'item_category','item_name','custom_item_name','FS_number', 'credit_paid', 'Transferred_from_bank_name',
            'Transferred_from_sender_name','Transferred_from_account_number', 'Transferred_to_bank_name', 'Transferred_to_receiver_name','Transferred_to_account_number',
            'serial_number', 'model', 'color', 'brand', 'quantity', 'unit', 'seller_name', "Receipt",'unit_price_before_vat', 
            'status', 'date_of_purchase', 'date_of_purchase_ethiopian', 'remark'
        ]
    
    custom_item_name = forms.CharField(required=False, max_length=100)
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
    
  
   
    remark = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 2}))
    
    

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('item_name')
        custom_item_name = cleaned_data.get('custom_item_name')

        if name == 'Other' and not custom_item_name:
            raise forms.ValidationError("Please provide a custom name if 'Other' is selected.")
        
        return cleaned_data
