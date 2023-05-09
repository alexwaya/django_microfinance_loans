from django import forms

from .models import Loans, Application

class AddLoanForm(forms.ModelForm):
    class Meta:
        model = Loans
        fields = [
            'loan_title',
            'loan_description',

            'interest',
            'thumbnail',
        ]

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            #'apply_reason',

            'amount_applied',
            'period_applied',
            'total_applied',

            'status',
        ]



