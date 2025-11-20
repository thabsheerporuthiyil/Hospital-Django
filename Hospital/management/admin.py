from django.contrib import admin

# Register your models here.
from .models import Departments,Doctor

admin.site.register(Departments)
admin.site.register(Doctor)
