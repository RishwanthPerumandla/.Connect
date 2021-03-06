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

class buyerForm(forms.Form):
	name = forms.CharField(required=False, max_length=100)
	email = forms.EmailField(required=True)
	Phone_Number = forms.IntegerField(required=True)
	description = forms.CharField(required=True, widget=forms.Textarea)