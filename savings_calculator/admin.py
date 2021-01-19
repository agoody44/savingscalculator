from django.contrib import admin
from .models import SavingsCalculator, CalculateSavings

# Register your models here.
admin.site.register(SavingsCalculator)
admin.site.register(CalculateSavings)

# admin.site.register(Item)
