from django.contrib import admin
from .models import Advertisement
@admin.register(Advertisement)
class Admin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status', 'creator', 'created_at']