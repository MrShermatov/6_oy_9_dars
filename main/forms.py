from django import forms
from .models import Cars, Models

class CarForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'

        widgets = {
            'car_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'car_year': forms.DateInput(attrs={
                'class': 'form-control',
            }),

            'car_price': forms.NumberInput(attrs={
                'class': 'form-control',

            }),

            'car_color': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'car_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5
            }),

            'car_image': forms.FileInput(attrs={'class': 'form-control'}),
            'car_model': forms.Select(attrs={'class': 'form-select'}),
        }

class ModelForm(forms.ModelForm):
    class Meta:
        model = Models
        fields = '__all__'

        widgets = {
            'model_name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand_loga': forms.FileInput(attrs={'class': 'form-control'}),
            'brand_countr': forms.TextInput(attrs={'class': 'form-control'}),
        }

