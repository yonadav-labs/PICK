from django import forms
from django.forms import ModelForm
from .models import *


class OrderForm(ModelForm):
    phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$', 
        error_messages = {'invalid': "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."})
	

    class Meta:
		model = Order
		exclude = ('owner', 'dropoff_addr', 'key', 'status')
	
