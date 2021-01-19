from django import forms
from django.forms import ModelForm
from .models import models


class CalculateSavings(forms.Form):
    wage = forms.CharField(label='Hourly Wage', max_length=200)
    bills = forms.CharField(label='Monthly Bills', max_length=200)

