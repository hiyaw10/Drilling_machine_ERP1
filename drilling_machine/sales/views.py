from rest_framework import viewsets
from .models import Contract, Project, SalesRecord, BankTransferDetail

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum

@api_view(['GET'])
def sales_report(request):
    fs_number = request.query_params.get('fs_number')
    buyer_name = request.query_params.get('buyer_name')
    tin_number = request.query_params.get('tin_number')

    sales_records = SalesRecord.objects.all()

    if fs_number:
        sales_records = sales_records.filter(fs_number=fs_number)
    if buyer_name:
        sales_records = sales_records.filter(buyer_name__icontains=buyer_name)
    if tin_number:
        sales_records = sales_records.filter(tin_number=tin_number)

    total_sales = sales_records.aggregate(total=Sum('total_price_including_vat'))
    
    return Response({
        'total_sales': total_sales['total'],
        'records': SalesRecordSerializer(sales_records, many=True).data,
    })
from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def contracts(request):
    # Logic for handling contract data will go here
    return render(request, 'contracts.html')

def projects(request):
    # Logic for handling project data will go here
    return render(request, 'projects.html')

def sales_records(request):
    # Logic for handling sales record data will go here
    return render(request, 'sales_records.html')

def bank_transfers(request):
    # Logic for handling bank transfer data will go here
    return render(request, 'bank_transfers.html')

def reports(request):
    # Logic for generating report data will go here
    return render(request, 'reports.html')    