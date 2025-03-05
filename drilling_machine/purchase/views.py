from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Item
from .forms import ItemForm, ReportForm
from decimal import Decimal

# Add Item View
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            print(f"Item saved: {item}")  # Debugging
            return redirect('purchase:generate_report')  
        else:
            print(form.errors)
            return render(request, 'purchase/add_item.html', {'form': form, 'errors': form.errors})
    else:
        form = ItemForm()
        form.fields['custom_item_name'].initial = 'Enter a custom name here if needed'

    return render(request, 'purchase/add_item.html', {'form': form})

import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UploadFileForm
from .models import Item

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            try:
                if file.name.endswith('.csv'):
                    data = pd.read_csv(file)
                elif file.name.endswith('.xlsx'):
                    data = pd.read_excel(file)
                else:
                    messages.error(request, 'Invalid file format. Please upload a CSV or Excel file.')
                    return redirect('upload_file')

                # Iterate over the rows and create Purchase objects
                for index, row in data.iterrows():
                    Purchase.objects.create(
                        FS_number=row['FS_number'],
                        Receipt=row['Receipt'],
                        item_name=row['item_name'],
                        custom_item_name=row.get('custom_item_name', ''),
                        item_category=row['item_category'],
                        payment_type=row['payment_type'],
                        payment_transaction_type=row.get('payment_transaction_type', ''),
                        remark=row.get('remark', ''),
                        unit_price_before_vat=row['unit_price_before_vat'],
                        status=row.get('status', ''),
                        quantity=row['quantity'],
                        unit=row['unit'],
                        seller_name=row.get('seller_name', ''),
                        total_price=row.get('total_price', None),
                        date_of_purchase=row['date_of_purchase'],
                        receipt_status=row.get('receipt_status', ''),
                        date_of_bank_transfer=row.get('date_of_bank_transfer', None),
                        serial_number=row.get('serial_number', ''),
                        item_destination=row['item_destination'],
                        model=row.get('model', ''),
                        color=row.get('color', ''),
                        brand=row.get('brand', ''),
                        Transferred_to_bank_name=row.get('Transferred_to_bank_name', ''),
                        Transferred_from_bank_name=row.get('Transferred_from_bank_name', ''),
                        Transferred_to_account_number=row.get('Transferred_to_account_number', ''),
                        Transferred_from_account_number=row.get('Transferred_from_account_number', ''),
                        Transferred_to_receiver_name=row.get('Transferred_to_receiver_name', ''),
                        Transferred_from_sender_name=row.get('Transferred_from_sender_name', ''),
                        USD_rate=row.get('USD_rate', None),
                        total_price_usd=row.get('total_price_usd', None)
                    )

                messages.success(request, 'File uploaded and data imported successfully.')
            except Exception as e:
                messages.error(request, f'Error processing file: {str(e)}')
            return redirect('upload_file')
    else:
        form = UploadFileForm()
    return render(request, 'purchase/upload.html', {'form': form})

# Generate Report View
from django.shortcuts import render, redirect
from django.db.models import Sum, F
from .models import Item
from .forms import ItemForm, ReportForm
from decimal import Decimal

VAT_RATE = Decimal("0.15")  # 15% VAT

from django.db.models import Sum
from decimal import Decimal

def generate_report(request):
    items = Item.objects.all()
    form = ReportForm(request.GET or None)

    # Fetch distinct values and remove duplicates
    categories = sorted(set(Item.objects.exclude(item_category__isnull=True).values_list('item_category', flat=True)))
    statuses = sorted(set(Item.objects.exclude(status__isnull=True).values_list('status', flat=True)))
    receipts = sorted(set(Item.objects.exclude(Receipt__isnull=True).values_list('Receipt', flat=True)))
    sellers = sorted(set(Item.objects.exclude(seller_name__isnull=True).values_list('seller_name', flat=True)))
    item_names = sorted(set(Item.objects.exclude(item_name__isnull=True).values_list('item_name', flat=True)))

    if form.is_valid():
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')
        category = request.GET.get('item_category', '').strip()
        status = request.GET.get('status', '').strip()
        receipt = request.GET.get('receipt', '').strip()  # Use 'receipt' (lowercase)
        seller_name = request.GET.get('seller_name', '').strip()
        item_name = request.GET.get('item_name', '').strip()

        # Debugging: Print form data and query parameters
        print(f"Form data: {form.cleaned_data}")
        print(f"Query parameters: {request.GET}")
        print(f"Receipt filter value: '{receipt}'")

        if start_date and end_date:
            items = items.filter(date_of_purchase__range=[start_date, end_date])
        if category:
            items = items.filter(item_category__iexact=category)  # Case-insensitive filtering
        if status:
            items = items.filter(status__iexact=status)  # Case-insensitive filtering
        if receipt:
            items = items.filter(Receipt__iexact=receipt)  # Case-insensitive filtering
        if seller_name:
            items = items.filter(seller_name__iexact=seller_name)  # Case-insensitive filtering
        if item_name:
            items = items.filter(item_name__iexact=item_name)  # Case-insensitive filtering

        # Debugging: Print filtered items count
        print(f"Filtered items count: {items.count()}")

    total_spent = round(items.aggregate(total=Sum('total_price'))['total'] or Decimal(0), 2)

    return render(request, 'purchase/report.html', {
        'items': items,
        'form': form,
        'categories': categories,
        'statuses': statuses,
        'receipts': receipts,
        'sellers': sellers,
        'item_names': item_names,
        'total_spent': total_spent,
    })