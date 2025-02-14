from django.urls import path
from . import views

app_name = 'items_used'

urlpatterns = [
    path('add/', views.add_items_used, name='add_items_used'),
    path('report/', views.items_used_report, name='items_used_report'),
]
