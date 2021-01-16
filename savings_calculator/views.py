from django.http import HttpResponse
from django.shortcuts import render
from .forms import CalculateSavings

def home(request):
    #return HttpResponse("Hello, Welcome!")
    return render(request, 'home.html')

def create (response):
    form = CalculateSavings()
    return render(response, 'create.html', {'form':form})
