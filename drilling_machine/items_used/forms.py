from django import forms
from .models import ItemsUsed

class ItemsUsedForm(forms.ModelForm):
    class Meta:
        model = ItemsUsed
        fields = ['inventory_item', 'quantity_used', 'date_of_use', 'person_responsible','description']
