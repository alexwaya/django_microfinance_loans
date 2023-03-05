from django.urls import path
from .views import * 

urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),
    # path('job/<int:job_id>/', view_dashboard_job, name="view_dashboard_job"),
    # path('application/<int:application_id>/', view_application, name="view_application"),

    # path('applications/', all_applications, name="all_applications"),

    # path('user-profiles/', user_profile, name="user_profile"),
]