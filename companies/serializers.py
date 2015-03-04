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
        fields  = ('id','name', 'color', 'company',)

class CompaniesSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Companies
        fields = ('id','name', 'thumb', 'owner', 'hash_id',)

class CompaniesRetrieveSerializer (serializers.ModelSerializer):
    owner = UserSerializer
    class Meta: 
        model = Companies
        fields = ('id', 'name', 'thumb', 'owner', 'hash_id',)

class MembersSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Members
        fields = ('id', 'member', 'company', 'role', 'hash_id',)

class MembersRetrieveSerializer (serializers.ModelSerializer):
    role = RolesSerializer(read_only = True)
    member = UserSerializer(read_only = True)
    company = CompaniesSerializer(read_only = True)
    class Meta: 
        model = Members
        fields = ('id', 'member', 'company', 'role', 'hash_id',)


