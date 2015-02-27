from rest_framework import serializers
from projects.models import Projects
from company.serializers import CompaniesSerializer

class ProjectSerializer (serializers.ModelSerializer):
    model = Projects
    company = CompaniesSerializer(read_only = True)
    fields = ('name', 'company', 'hash_id', )
