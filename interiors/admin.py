from django.contrib import admin
from .models import *

@admin.register(AdvUser)
class AdvUserAdmin(admin.ModelAdmin):
    fields = ("first_name", "last_name", "patronymic", "username", "email", "password", "role", "date_joined", "last_login",
              "is_superuser", "groups", "user_permissions", "is_staff", "is_active")
