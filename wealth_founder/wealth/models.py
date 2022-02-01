from django.db import models
from datetime import datetime,date
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
import urllib
from django.core.files import File
import os
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Profile(AbstractUser, PermissionsMixin):
    firstname = models.CharField( max_length=50,null=True)
    lastname = models.CharField(max_length=50,null=True)
    dob = models.DateField(auto_now=False, auto_now_add=False,null=True)
    username = models.CharField(max_length=25, primary_key=True)
    mobile = models.CharField(unique=False,max_length=15,null= True)
    address = models.TextField(blank=True, null=True)
    # city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=50,null=True)
    is_superuser = models.BooleanField(blank=True, default=False,null=True)
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=50,null=True)