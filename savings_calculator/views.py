from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import CalculateSavings
from .models import SavingsCalculator

# def index(response):
#     return render(request,'index.html')


def home(request):
    #return HttpResponse("Hello, Welcome!")
    return render(request, 'home.html')

def calculate (request):

    if request.method == 'POST':
        form = CalculateSavings(request.POST)
        if form.is_valid():
            # form.save()
            # return redirect('calculate')
            # request.session['CalculateSavings_input'] = request.POST['CalculateSavings_input']
            # return redirect('savings_url')
            

            wage = form.cleaned_data['wage']
            bills = form.cleaned_data['bills']

            print(wage, bills)

    form = CalculateSavings()
    return render(request, 'calculate.html', {'form' : form})


def savings(request):
    #return HttpResponse("Hello, Welcome!")
    # url = request.session.get('CalculateSavings_input')
    return render(request, 'savings.html')