from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Loan
from .forms import LoanForm, PaymentForm

@login_required
def loan_create(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            loan.user = request.user
            loan.save()
            return redirect('loan_list')
    else:
        form = LoanForm()
    return render(request, 'loans/loan_form.html', {'form': form})

@login_required
def loan_list(request):
    loans = Loan.objects.all()
    return render(request, 'loans/loan_list.html', {'loans': loans})

@login_required
def loan_create(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            loan.user = request.user
            loan.save()
            return redirect('loan_list')
    else:
        form = LoanForm()
    return render(request, 'loans/loan_form.html', {'form': form,  'error': 'You need to be logged in to create a loan'})

@login_required
def loan_detail(request, pk):
    loan = Loan.objects.get(pk=pk)
    remaining_balance = loan.total()
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment_amount = form.cleaned_data['payment_amount']
            remaining_balance -= payment_amount
            loan.status = 'Paid' if loan.amount <= payment_amount else 'Partially Paid'
            loan.save()
            return redirect('loan_detail', pk=pk)
    else:
        form = PaymentForm()
    return render(request, 'loans/loan_detail.html', {'loan': loan, 'form': form, 'remaining_balance': remaining_balance})

@login_required
def loan_update(request, pk):
    loan = Loan.objects.get(pk=pk)
    if request.method == 'POST':
        form = LoanForm(request.POST, instance=loan)
        if form.is_valid():
            form.save()
            return redirect('loan_detail', pk=pk)
    else:
        form = LoanForm(instance=loan)
    return render(request, 'loans/loan_form.html', {'form': form})

@login_required
def loan_delete(request, pk):
    loan = Loan.objects.get(pk=pk)
    if request.method == 'POST':
        loan.delete()
        return redirect('loan_list')
    return render(request, 'loans/loan_confirm_delete.html', {'loan': loan})