# inventory/urls.py
from django.urls import path
from . import views
app_name = 'inventory' 

urlpatterns = [
    path('inventory/', views.inventory_list, name='inventory_list'),
]
