from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Item
from .forms import ItemForm, ReportForm
from decimal import Decimal







# Add Item View
from django.shortcuts import render, redirect
from django.db.models import F
from .models import Item
from .forms import ItemForm, ReportForm
from decimal import Decimal

# Add Item View
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            print(f"Item saved: {item}")  # Debugging
            return redirect('purchase:generate_report')  
        else:
            print(form.errors)
            return render(request, 'purchase/add_item.html', {'form': form, 'errors': form.errors})
    else:
        form = ItemForm()
        form.fields['custom_name'].initial 

    return render(request, 'purchase/add_item.html', {'form': form})


def generate_report(request):
    items = Item.objects.all()
    form = ReportForm(request.GET)
    
    if form.is_valid():
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        category = form.cleaned_data['item_class'] 
            
        # Filter items based on form data
        if category:
            items = items.filter(item_class=category)
        items = items.filter(date_of_purchase__range=[start_date, end_date])

    total_spent = round(items.aggregate(total=Sum('total_price'))['total'] or 0, 2)
    return render(request, 'purchase/report.html', {'form': form, 'items': items, 'total_spent': total_spent})


def generate_report(request):
    items = Item.objects.all()
    form = ReportForm(request.GET)
    
    if form.is_valid():
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        category = form.cleaned_data['item_class'] 
            
        # Filter items based on form data
        if category:
            items = items.filter(item_class=category)
        items = items.filter(date_of_purchase__range=[start_date, end_date])

    total_spent = round(items.aggregate(total=Sum('total_price'))['total'] or 0, 2)
    return render(request, 'purchase/report.html', {'form': form, 'items': items, 'total_spent': total_spent})