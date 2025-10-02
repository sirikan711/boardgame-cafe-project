# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    fullname = models.CharField(max_length=255, blank=True, null=True) # แนะนำให้เพิ่ม blank=True, null=True
    role = models.CharField(max_length=20, default='staff') 

    def __str__(self):
        return self.username