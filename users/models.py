from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """ User Model """
    
    name = models.CharField(max_length=140, blank=False)
    email = models.CharField(max_length=250, blank=False)

    def __str__(self):
      return self.username