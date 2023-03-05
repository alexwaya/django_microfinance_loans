from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login

from .models import Loans
from .forms import AddLoanForm, ApplicationForm

def all_loans(request):
    loans = Loans.objects.all().order_by('-created_at')
    context = {
        "loans": loans,
    }
    return render(request, 'loans/all_loans.html', context)


def loan_detail(request, loan_id):
    loan = Loans.objects.get(pk=loan_id)
    context = {
        "loan": loan,
    }
    return render(request, 'loans/loan_detail.html', context)


@login_required
def add_loan(request):
    if request.method == 'POST':
        form = AddLoanForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            loan.created_by = request.user
            loan.save()
            return redirect('dashboard')
    else:
        form = AddLoanForm()
    context = {
        "form": form,
    }
    return render(request, 'loans/add_loan.html', context)


@login_required
def apply_for_loan(request, loan_id):
    loan = Loans.objects.get(pk=loan_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.loan = loan
            application.created_by = request.user
            application.save()
            #create_notification(request, job.created_by, 'application', extra_id=application.id)
            return redirect('dashboard')
    else:
        form = ApplicationForm()
    context = {
        "job": loan,
        "form": form,
    }
    return render(request, 'loans/apply_for_loan.html', context)






