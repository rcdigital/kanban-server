from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.response import Response

from django.http import Http404

from projects.serializers import ProjectSerializer, ProjectSerializerRetrieve
from projects.models import Projects

from backlog.models import Backlogs

class ProjectList(APIView):
    def get(self, request, company_pk, format=None):
        queryset = Projects.objects.filter(company__id= company_pk)  
        serializer = ProjectSerializerRetrieve(queryset, many= True)
        return Response(serializer.data)

    def post(self, request, company_pk, format=None):
        serializer = ProjectSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ProjectDetails(APIView):
    def get_object(self, project_id, format=None):
        try:
            return Projects.objects.get(id = project_id)
        except Projects.DoesNotExist:
            return Http404

    def put(self, request, project_id):
        project = self.get_object(project_id)
        serializer = ProjectSerializer(project, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def get(self, request, project_id):
        project = self.get_object(project_id)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def delete(self, request, project_id):
        project = self.get_object(project_id)
        project.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
