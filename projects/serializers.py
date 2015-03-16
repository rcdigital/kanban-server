from rest_framework import serializers
from projects.models import Projects
from companies.serializers import CompaniesRetrieveSerializer

class ProjectSerializerRetrieve (serializers.ModelSerializer):
    company = CompaniesRetrieveSerializer(read_only = True)
    class Meta: 
        model = Projects
        fields = ('name', 'company', 'hash_id', )

class ProjectSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Projects
        fields = ('id' ,'name', 'company',)
