from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

#from jobs.models import Jobs, Application
from userprofile.models import *

#from notification.utilities import create_notification

@login_required
def dashboard(request):
    context = {
        "userprofile": request.user.userprofile,
        }
    return render(request, 'userprofile/index_dashboard.html', context)