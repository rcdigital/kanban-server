from rest_framework import serializers
from companies.models import Companies, Members, Roles
from users.serializers import UsersSerializer

class RolesSerializer (serializers.ModelSerializer):
    model = Roles
    fields  = ('name', 'color',)

class MembersSerializer (serializers.ModelSerializer):
    model = Members
    member = UsersSerializer(read_only = True)
    role = RolesSerializer(read_only = True)
    fields = ('member', 'role', 'hash_id',)

class CompaniesSerializer (serializers.ModelSerializer):
    model = Companies
    members = MembersSerializer(many = True, read_only = True)
    owner = UsersSerializer(read_only = True)
    fields = ('name', 'thumb', 'owner', 'hash_id', 'members',)
