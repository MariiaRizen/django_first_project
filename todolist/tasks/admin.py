from django.contrib import admin

# Register your models here.
from django.contrib import admin
from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'done')
    search_fields = ['title']



