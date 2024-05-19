from django import forms
from .models import Loan

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['name','amount', 'interest_rate', 'term_year', 'start_date']

class PaymentForm(forms.Form):
    payment_amount = forms.DecimalField(label='Payment Amount', max_digits=10, decimal_places=2)
    