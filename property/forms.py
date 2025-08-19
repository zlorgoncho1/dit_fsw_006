from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'price', 'image', 'surface', 'rooms', 'bathrooms', 'garage', 'garden', 'city']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre du bien'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.TextInput(attrs={'class': 'form-control'}),
            'surface': forms.NumberInput(attrs={'class': 'form-control'}),
            'rooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'bathrooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'garage': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'garden': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError("Le prix ne peut pas être négatif")
        return price