# data_visualization_app/forms.py

from django import forms
from .models import EnvironmentalData, SocialData

class EnvironmentalDataForm(forms.ModelForm):
    class Meta:
        model = EnvironmentalData
        fields = '__all__'

class SocialDataForm(forms.ModelForm):
    class Meta:
        model = SocialData
        fields = '__all__'
