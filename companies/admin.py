from django.contrib import admin
from companies.models import Companies, Roles, Members

class MembersStackedInline(admin.StackedInline):
    model = Members 
    extra = 1

class RolesStackedInline(admin.StackedInline):
    model = Roles
    extra = 1

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', )
    inlines = [RolesStackedInline, MembersStackedInline,]


admin.site.register(Companies, CompanyAdmin)
