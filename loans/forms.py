from django import forms

from .models import Loans, Application

class AddLoanForm(forms.ModelForm):
    class Meta:
        model = Loans
        fields = [
            'loan_title',
            'loan_description',
        ]

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'apply_reason',
        ]



