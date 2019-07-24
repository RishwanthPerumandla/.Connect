from django import forms


class buyerForm(forms.Form):
	name = forms.CharField(required=False, max_length=100)
	email = forms.EmailField(required=True)
	Phone_Number = forms.IntegerField(required=True)
	description = forms.CharField(required=True, widget=forms.Textarea)
		