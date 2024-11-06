from django.contrib import admin

# Register your models here.
# admin.py
from django.contrib import admin
from .models import Payment

admin.site.register(Payment)

