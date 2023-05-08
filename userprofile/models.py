from django.db import models
from django.contrib.auth.models import User

from pages.models import CustomUser

class Userprofile(models.Model):
    user = models.OneToOneField(CustomUser, related_name='userprofile', on_delete=models.CASCADE)
    is_employer = models.BooleanField(default=False)



#Check if user exists, if not create
CustomUser.userprofile = property(lambda u:Userprofile.objects.get_or_create(user=u)[0])





