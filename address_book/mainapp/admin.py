# Register your models here.
from django.forms import ModelChoiceField   # import forms
from django.contrib import admin
from .models import *   # import all models here
admin.site.register(Users)
