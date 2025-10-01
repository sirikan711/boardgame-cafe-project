# boardgames/admin.py
from django.contrib import admin
from .models import BoardGame

admin.site.register(BoardGame)