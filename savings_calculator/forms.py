from django import forms


class CalculateSavings(forms.Form):
    wage = forms.CharField(label='Hourly Wage', max_length=200)
