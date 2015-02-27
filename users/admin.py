from django.contrib import admin
from users.models import KanbanUsers

class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)



admin.site.register(KanbanUsers, UsersAdmin)
