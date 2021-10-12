from django.contrib import admin
from .models import Users   # import models here

admin.site.register(Users)   # Регистрация поля в админке
