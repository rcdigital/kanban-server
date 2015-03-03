from rest_framework import serializers
from users.models import KanbanUsers 
from companies.serializers import CompaniesSerializer



class UsersSerializer(serializers.ModelSerializer):
    companies = CompaniesSerializer(many = True, read_only = True)
    class Meta:
        model = KanbanUsers 
        fields = ('id', 'name', 'email', 'thumb', 'companies',)
