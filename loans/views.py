from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login

from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)

from .models import Loans, Application
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
def loan_detail_admin(request, loan_id):
    context = {}
    context["loan"] = Loans.objects.get(pk=loan_id)
    # loan = Loans.objects.get(pk=loan_id)
    # context = {
    #     "loan": loan,
    # }
    return render(request, 'loans/loan_detail_admin.html', context)

@login_required
def update_loans_admin(request, id):
    loan = Loans.objects.get(id=id)

    form = AddLoanForm(request.POST, request.FILES, instance=loan) 
    if request.method == 'POST':
        if form.is_valid():
            formupdate = form.save(commit=False)
            formupdate.save() 
            return redirect('all_loans_admin')
        else:
            print("------s-s-s-ssssss----")
            print(form.errors.as_data()) # here you print errors to terminal
    else:
        form = AddLoanForm(instance=loan)
    context = {
        "loan": loan,
        "form": form,
    }
    return render(request, 'loans/update_loans_admin.html', context)


@login_required
def loan_delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Loans, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return redirect('all_loans_admin')
 
    return render(request, "loans/loan_delete_view.html", context)




@login_required
def add_loan(request):
    form = AddLoanForm(request.POST, request.FILES)
    if request.method == 'POST':
        
        if form.is_valid():
            loan = form.save(commit=False)
            loan.created_by = request.user
            loan.save()
            return redirect('all_loans_admin')
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
        "loan": loan,
        "job": loan,
        "form": form,
    }
    return render(request, 'loans/apply_for_loan.html', context)



@login_required
def all_applications(request):
    applications = Application.objects.all().order_by('-created_at')
    context = {
        "applications": applications,
    }
    return render(request, 'loans/all_applications.html', context)




@login_required
def all_loans_admin(request):
    context = {
        "userprofile": request.user.userprofile,
        }
    return render(request, 'loans/all_loans_admin.html', context)



@login_required
def loan_application_review(request, id):
    application = Application.objects.get(id=id)

    form = ApplicationForm(request.POST, request.FILES, instance=application) 
    if request.method == 'POST':
        if form.is_valid():
            formupdate = form.save(commit=False)
            formupdate.save() 
            return redirect('dashboard')
        else:
            print("------s-s-s-ssssss----")
            print(form.errors.as_data()) # here you print errors to terminal
    else:
        form = ApplicationForm(instance=application)
    context = {
        "application": application,
        "form": form,
    }
    return render(request, 'loans/loan_application_review.html', context)