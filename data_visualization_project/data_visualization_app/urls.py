# data_visualization_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-environmental-data/', views.add_environmental_data, name='add_environmental_data'),
    path('add-social-data/', views.add_social_data, name='add_social_data'),
    path('api/environmental_data/', views.get_environmental_data, name='get_environmental_data'),
]
