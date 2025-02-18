from django.shortcuts import render, redirect
from django.db.models import Sum
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
        # If needed, set a default initial value for 'custom_name'
        form.fields['custom_item_name'].initial = 'Enter a custom name here if needed'

    return render(request, 'purchase/add_item.html', {'form': form})



def generate_report(request):
    items = Item.objects.all()
    form = ReportForm(request.GET)

    # Get distinct categories & statuses for dropdowns
    categories = Item.objects.values_list('item_category', flat=True).distinct()
    statuses = Item.objects.values_list('status', flat=True).distinct()
    

    if form.is_valid():
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')
        category = request.GET.get('item_category', None)
        status = request.GET.get('status', None)

        if start_date and end_date:
            items = items.filter(date_of_purchase__range=[start_date, end_date])

        if category:
            items = items.filter(item_category=category)

        if status:
            items = items.filter(status=status)

    total_spent = round(items.aggregate(total=Sum('total_price'))['total'] or 0, 2)

    return render(
        request, 
        'purchase/report.html', 
        {
            'form': form, 
            'items': items, 
            'total_spent': total_spent, 
            'categories': categories, 
            'statuses': statuses
        }
    )

