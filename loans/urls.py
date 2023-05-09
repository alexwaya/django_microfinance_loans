from django.urls import path
from .views import * 

urlpatterns = [
    path('loans/', all_loans, name="all_loans"),
    path('loans/<int:loan_id>/details', loan_detail, name="loan_detail"),
    path('loans/<int:loan_id>/apply/', apply_for_loan, name="apply_for_loan"),

    path('dashboard/loans/add/', add_loan, name="add_loan"),
    path('dashboard/loans/all/', all_loans_admin, name="all_loans_admin"),

    path('dashboard/loans/<int:loan_id>/details', loan_detail_admin, name="loan_detail_admin"),

    path('dashboard/loans/<int:id>/update', update_loans_admin, name="update_loans_admin"),
    path('dashboard/loans/<int:id>/delete', loan_delete_view, name="loan_delete_view"),
]