from django.contrib import admin
from backlog.models import Backlogs, Stories
from tasks.models import Tasks

class StoriesStackedInline(admin.StackedInline):
    model = Stories
    extra = 1

class TasksStackedInline(admin.StackedInline):
    model = Tasks
    extra = 1

class BacklogAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', )
    inlines = [StoriesStackedInline,]

class StoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [TasksStackedInline,]

admin.site.register(Backlogs, BacklogAdmin)
admin.site.register(Stories, StoriesAdmin)
