from django.db import models

# Create your models here.
# class SavingsCalculator(models.Model):
#     wage = models.CharField(max_length=200)
#     bills = models.CharField(max_length=200)

#     def __str__(self):
#         return self.wage


class CalculateSavings(models.Model):
    wage = models.CharField(max_length=200)
    bills = models.CharField(max_length=200)
    # daily = models.DecimalField(max_digits=6, decimal_places=4)
    # weekly = models.DecimalField(max_digits=6, decimal_places=4)
    # monthly = models.DecimalField(max_digits=6, decimal_places=4)

    def __str__(self):
        return self.wage





# class Item(models.Model):
#     SavingsCalculator = models.ForeignKey(SavingsCalculator, on_delete=models.CASCADE)
#     text = models.CharField(max_length=300)
#     complete = models.BooleanField()

#     def __str__(self):
#         return self.text