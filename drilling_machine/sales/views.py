from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, SalesRecord
from .forms import ProjectForm, SalesRecordForm
from django.db.models import Q

# Business List Page
def business_list(request):
    businesses = Project.objects.all()
    return render(request, 'sales/business_list.html', {'businesses': businesses})

# Business Form
def add_business(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('business_list')
    else:
        form = ProjectForm()
    return render(request, 'sales/add_business.html', {'form': form})

# Sales Entry Form
def daily_sales(request):
    if request.method == "POST":
        form = SalesRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sales_report')
    else:
        form = SalesRecordForm()
    return render(request, 'sales/daily_sales.html', {'form': form})

# Business Contract Check Page
def contract_check(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'sales/contract_check.html', {'project': project})

# Sales Report Page
def sales_report(request):
    sales = SalesRecord.objects.all()
    
    # Filtering
    fs_number = request.GET.get('fs_number', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    buyer_name = request.GET.get('buyer_name', '')
    tin_number = request.GET.get('tin_number', '')
    bank_from = request.GET.get('bank_from', '')
    bank_to = request.GET.get('bank_to', '')

    if fs_number:
        sales = sales.filter(fs_number__icontains=fs_number)
    if start_date and end_date:
        sales = sales.filter(date__range=[start_date, end_date])
    if buyer_name:
        sales = sales.filter(buyer_name__icontains=buyer_name)
    if tin_number:
        sales = sales.filter(tin_number__icontains=tin_number)
    if bank_from:
        sales = sales.filter(bank_transferred_from_name__icontains=bank_from)
    if bank_to:
        sales = sales.filter(bank_transferred_to_name__icontains=bank_to)

    return render(request, 'sales/sales_report.html', {'sales': sales})
