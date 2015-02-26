from django.contrib import admin
from projects.models import Projects

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'company',)

admin.site.register(Projects, ProjectsAdmin)
