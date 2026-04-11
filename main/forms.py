from django import forms
from .models import Cars, Models

class CarForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'

class ModelForm(forms.ModelForm):
    class Meta:
        model = Models
        fields = '__all__'
