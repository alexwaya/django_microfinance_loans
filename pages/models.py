from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    email_id = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=255)
    id_no = models.CharField(max_length=255)

    #cv = models.FileField(upload_to='cvs/', blank=True, null=True, default='')

    def __str__(self):
        return self.first_name
    


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    subject = models.CharField(max_length=1024)
    message = models.TextField()


    def __str__(self):
        return self.name