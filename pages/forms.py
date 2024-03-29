from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Contact

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            "username", 
            "email_id", 
            "first_name", 
            "last_name", 
            "phone_no", 
            'id_no',
            )

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = (
            "username", 
            "email_id", 
            "first_name", 
            "last_name", 
            "phone_no", 
            'id_no',
            )
        


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'subject',
            'message',
        ]

