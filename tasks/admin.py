from django.contrib import admin
from tasks.models import Tasks 

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Tasks, TaskAdmin)
