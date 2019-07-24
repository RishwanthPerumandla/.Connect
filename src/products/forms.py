from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'category', 
            'image',
            'email',
        ]



class ImageForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image',]