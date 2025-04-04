from django import forms
from .models import Wishlist

class ListForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['title', 'image', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}),
        }