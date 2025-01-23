from django.contrib import admin

# Register your models here.
from .models import CV

@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'data', 'created_at']