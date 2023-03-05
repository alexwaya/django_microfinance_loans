from django.urls import path
from .views import * 

urlpatterns = [
    path('all-loans/', all_loans, name="all_loans"),
    path('more-details/<int:loan_id>/', loan_detail, name="loan_detail"),
    path('loans/', add_loan, name="add_loan"),
    path('loans/<int:loan_id>/apply/', apply_for_loan, name="apply_for_loan"),
]