from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from userprofile.models import Userprofile
from loans.models import Loans

from pages.forms import CustomUserCreationForm

from django.contrib.auth.decorators import login_required
from pages.models import CustomUser
from django.shortcuts import (get_object_or_404, render)

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
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
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
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, 'registration/signup.html', context)



@login_required
def user_profile(request, id):
    user = CustomUser.objects.get(id=id)

    form = CustomUserCreationForm(request.POST, request.FILES, instance=user) 
    if request.method == 'POST':
        if form.is_valid():
            formupdate = form.save(commit=False)
            formupdate.save() 
            return redirect('user_profile')
        else:
            print("------s-s-s-ssssss----")
            print(form.errors.as_data()) # here you print errors to terminal
    else:
        form = CustomUserCreationForm(instance=user)
    context = {
        "user": user,
        "form": form,
    }
    return render(request, 'registration/user_profile.html', context)