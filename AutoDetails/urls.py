from django.urls import path, include
from django.views.generic import TemplateView
from .views import vehicleform

urlpatterns = [
    path('', vehicleform, name='Home'),
]