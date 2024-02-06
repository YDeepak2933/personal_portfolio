from django.contrib import admin

# Register your models here.
from .models import (
    Project
)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title","technology","description")
    search_fields = ("title","technology")
    list_filter = ("technology",)

admin.site.register(Project,ProjectAdmin)