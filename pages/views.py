from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def index_view(request):
    context = {}
    return render(request, 'pages/index.html', context)

def signup(request):
    # form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()

    #         account_type = request.POST.get('account_type', 'jobseeker')
    #         #account_type = request.POST.get('account_type')

    #         if account_type == 'employer':
    #             userprofile = Userprofile.objects.create(user=user, is_employer=True)
    #             userprofile.save()
    #         else:
    #             userprofile = Userprofile.objects.create(user=user)
    #             userprofile.save()

            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    context = {
        "form": form,
    }
    return render(request, 'registration/signup.html', context)


