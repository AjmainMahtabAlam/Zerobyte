from django.contrib import admin
from .models import Package

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'recipient', 'status', 'is_deleted', 'created_at')
    search_fields = ('sender', 'recipient', 'status')
    list_filter = ('status', 'is_deleted')
