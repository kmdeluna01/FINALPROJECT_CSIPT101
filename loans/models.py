from django.db import models
from django.contrib.auth.models import User

class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null = True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    term_year = models.IntegerField()
    start_date = models.DateField(default="yyyy-mm-dd")
    status = models.CharField(max_length=20, default='Pending')

    def total(self):
        total = self.amount * (1 + self.interest_rate / 100 * self.term_year)
        return round(total,2)
    
    def monthly_payment(self):
        interest_percentage = self.interest_rate / 100
        months = self.term_year * 12
        interest = self.amount * interest_percentage * self.term_year
        monthly = (self.amount + interest) / months
        return round(monthly,2)

    def __str__(self):
        return f'Loan {self.id} for {self.user.username} - {self.term_year} year'