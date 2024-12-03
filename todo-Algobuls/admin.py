from django.contrib import admin
from .models import TodoItem

@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'due_date', 'timestamp')
    list_filter = ('status', 'due_date')
    search_fields = ('title', 'description')
    readonly_fields = ('timestamp',)

# Register your models here.
