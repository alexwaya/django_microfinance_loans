from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login

from .models import Loans

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




