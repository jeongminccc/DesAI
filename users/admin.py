from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from . import models
from .models import User

# Register your models here.
admin.site.register(User)

