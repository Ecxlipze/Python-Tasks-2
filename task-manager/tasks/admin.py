from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "project",
        "completed",
        "created_at",
    )

    list_filter = (
        "completed",
        "project",
    )

    search_fields = (
        "title",
    )