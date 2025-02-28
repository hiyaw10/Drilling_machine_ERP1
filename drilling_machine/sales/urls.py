from django.urls import path
from . import views

urlpatterns = [
    path('businesses/', views.business_list, name='business_list'),
    path('businesses/add/', views.add_business, name='add_business'),
    path('sales/', views.daily_sales, name='daily_sales'),
    path('contract/<int:project_id>/', views.contract_check, name='contract_check'),
    path('sales/report/', views.sales_report, name='sales_report'),
]
