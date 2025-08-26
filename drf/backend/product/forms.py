from django import forms 
from .model import Product


class ProductForm(forms.ModelForm):
    class META:
        model = Product
        fields = [
            'title',
            'content',
            'price'
        ]
