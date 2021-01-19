from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import CalculateSavings


def home(request):
    return render(request, 'home.html')

def calculate (request):
    wage = None
    bills = None
    daily = None
    weekly = None
    monthly = None

    if request.method == 'POST':
        form = CalculateSavings(request.POST)
        if form.is_valid():


            wage = form.cleaned_data['wage']
            bills = form.cleaned_data['bills']
            daily = form.cleaned_data['bills']
            weekly = form.cleaned_data['bills']
            monthly = form.cleaned_data['bills']




            value = int(wage)

            daily = value * 8
            
            weekly = daily * 5
            
            monthly = weekly * 4
            
            value = int(bills)
            bills = monthly - value
            

            

            print(wage, bills, daily, weekly, monthly)

    form = CalculateSavings()
    return render(request, 'calculate.html', {'form' : form, 'wage' : wage, 'daily' : daily, 'weekly' : weekly, 'monthly': monthly, 'bills' : bills, } )


