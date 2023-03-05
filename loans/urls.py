from django.urls import path
from .views import * 

urlpatterns = [
    path('all-loans/', all_loans, name="all_loans"),
    path('more-details/<int:loan_id>/', loan_detail, name="loan_detail"),
    # path('add-job/', add_job, name="add_job"),
    # path('apply/<int:job_id>/', apply_for_job, name="apply_for_job"),
]