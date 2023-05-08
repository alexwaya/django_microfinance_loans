from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name="index_view"),
    path('signup/', signup, name="signup"),
    path('about-us/', about_us, name="about_us"),
    path('contact-us/', contact_us, name="contact_us"),
]