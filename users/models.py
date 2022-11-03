from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    birthdate = models.DateField()
    bio = models.TextField(null=True)
    is_critic = models.BooleanField(default=False, null=True)
    updated_at = models.DateTimeField(auto_now=True)


    REQUIRED_FIELDS = ["first_name","last_name", "birthdate"]


 

    