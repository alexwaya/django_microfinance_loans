from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from userprofile.models import Userprofile
from loans.models import Loans

# def index_view(request):
#     context = {}
#     return render(request, 'pages/index.html', context)

def index_view(request):
    loans = Loans.objects.all().order_by('-created_at')[0:3]
    context = {
        "loans": loans,
    }
    return render(request, 'pages/index.html', context)


def about_us(request):
    context = {}
    return render(request, 'pages/about_us.html', context)


def contact_us(request):
    context = {}
    return render(request, 'pages/contact_us.html', context)


def signup(request):
    # form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()

            account_type = request.POST.get('account_type', 'jobseeker')

            if account_type == 'employer':
                userprofile = Userprofile.objects.create(user=user, is_employer=True)
                userprofile.save()
            else:
                userprofile = Userprofile.objects.create(user=user)
                userprofile.save()

            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    context = {
        "form": form,
    }
    return render(request, 'registration/signup.html', context)


