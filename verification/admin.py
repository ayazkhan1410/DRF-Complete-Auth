from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):
    list_display = ['email', 'name', 'tc', 'is_active', 'is_admin', 'created_at', 'updated_at']
    search_fields = ['email', 'name', 'tc', 'is_active', 'is_admin', 'created_at', 'updated_at']
    list_filter = ['email', 'name', 'tc', 'is_active', 'is_admin', 'created_at', 'updated_at']
    list_per_page = 10
    ordering = ['id']
