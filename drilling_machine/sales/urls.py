from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import dashboard, contracts, projects, sales_records, bank_transfers, reports

urlpatterns = [
    path('', dashboard, name='dashboard'),  # Routing to the dashboard
    path('contracts/', contracts, name='contracts'),  # Routing to contracts page
    path('projects/', projects, name='projects'),  # Routing to projects page
    path('sales-records/', sales_records, name='sales_records'),  # Routing to sales records page
    path('bank-transfers/', bank_transfers, name='bank_transfers'),  # Routing to bank transfers page
    path('reports/', reports, name='reports'),  # Routing to reports page
]