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




            value = float(wage)
            daily = value * 8
            # dv_value.set("%.2f" % daily)
            weekly = daily * 5
            # wv_value.set("%.2f" % weekly)
            monthly = weekly * 4
            # mv_value.set("%.2f" % monthly)
            value = float(bills)
            bills = monthly - value
            # bv_value.set("%.2f" % bills)

            

            print(wage, bills, daily, weekly, monthly)

    form = CalculateSavings()
    return render(request, 'calculate.html', {'form' : form, 'wage' : wage, 'bills' : bills, 'daily' : daily, 'weekly' : weekly, 'monthly': monthly } )


