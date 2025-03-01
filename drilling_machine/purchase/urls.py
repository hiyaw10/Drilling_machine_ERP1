from django.urls import path
from . import views

app_name = 'purchase'  

urlpatterns = [
    path('report/', views.generate_report, name='generate_report'),
    path('add_item/', views.add_item, name='add_item'),  # URL for adding purchased goods
]


