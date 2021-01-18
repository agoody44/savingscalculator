from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import CalculateSavings
from .models import SavingsCalculator, Item

def index(response, id):    
    ls = SavingsCalculator.obects.get(id=id)
    return HttpResponse('<h1>%s</h1>' %ls.wage)


def home(request):
    #return HttpResponse("Hello, Welcome!")
    return render(request, 'home.html')

def create (request):

    if request.method == 'POST':
        form = CalculateSavings(request.POST)
        if form.is_valid():
            

            wage = form.cleaned_data['wage']
            bills = form.cleaned_data['bills']

            print(wage, bills)

    form = CalculateSavings()
    return render(request, 'create.html', {'form' : form})


def savings(request):
    #return HttpResponse("Hello, Welcome!")
    return render(request, 'savings.html')