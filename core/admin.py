"""This file contains UserAdmin model to introduce users in the django admin
panel"""
from django.contrib import admin
from core.models import User
# --------------------------------------------------------------------------


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """This class represents users in the django admin panel"""
    list_display = ('email', 'username', 'is_superuser', 'first_name',
                    'last_name')
    search_fields = ('email', 'username')
    list_filter = ('is_superuser', 'is_staff', 'is_active')
