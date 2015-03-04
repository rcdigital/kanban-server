from rest_framework import serializers
from users.models import KanbanUsers 
from companies.serializers import CompaniesRetrieveSerializer 



class UsersSerializer(serializers.ModelSerializer):
    companies = CompaniesRetrieveSerializer(many = True, read_only = True)
    class Meta:
        model = KanbanUsers 
        fields = ('id', 'name', 'email', 'thumb', 'companies',)

class UsersDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = KanbanUsers 
        fields = ('id', 'name', 'email', 'thumb',)
