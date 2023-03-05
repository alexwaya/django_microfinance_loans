from django.contrib import admin

from .models import Loans, Application

admin.site.register(Loans)
admin.site.register(Application)