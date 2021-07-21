from django import forms
from .models import VehicleDetails, EngineDetails

class VehicleForm(forms.ModelForm):
    class Meta:
        model = VehicleDetails
        fields = [
            'sap_code',
            'ledger_name',
            'manufacturer',
            'mno',
            'vehicle_type',
            'base_km',
            'rto'
        ]

class EngineForm(forms.ModelForm):
    class Meta:
        model = EngineDetails
        fields = [
            'model_year',
            'chassis_no',
            'fuel_type',
            'old_vehicle_no'
        ]