from rest_framework import serializers
from companies.models import Companies, Members, Roles
from users.models import KanbanUsers 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = KanbanUsers 
        fields = ('id', 'name', 'email', 'thumb', 'companies',)

class RolesSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Roles
        fields  = ('name', 'color',)

class MembersSerializer (serializers.ModelSerializer):
    role = RolesSerializer(read_only = True)
    class Meta: 
        model = Members
        fields = ('member', 'role', 'hash_id',)

class CompaniesSerializer (serializers.ModelSerializer):
    members = MembersSerializer(many = True, read_only = True)
    owner = UserSerializer(many= False, read_only = True)
    class Meta: 
        model = Companies
        fields = ('name', 'thumb', 'owner', 'hash_id', 'members',)
