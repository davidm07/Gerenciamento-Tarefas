from django.contrib import admin
from .models import Task
from api import models

# Register your models here.
@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'completed')
