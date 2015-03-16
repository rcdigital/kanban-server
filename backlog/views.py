from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from backlog.serializers import BacklogSerializer, BacklogSerializerRetrieve
from backlog.models import Backlogs

class BacklogList(APIView):
    def post(self, request, project_id, format=None):
        serializer = BacklogSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def get(self, request, project_id, format=None):
        queryset = Backlogs.objects.filter(project__id= project_id)  
        serializer = BacklogSerializerRetrieve(queryset, many= True)
        return Response(serializer.data)

class BacklogDetails(APIView):
    def get_object(self, project_id):
        try:
            return Backlogs.objects.filter(project = project_id)
        except Backlogs.DoesNotExist:
            raise Http404

    def get(self, request, company_pk, member_id, format=None):
        member = self.get_object(company_pk, member_id)  
        serializer = MembersRetrieveSerializer(member, many= True)
        return Response(serializer.data)

    def delete(self, request, company_pk, member_id, format=None):
        member = self.get_object(company_pk, member_id)
        member.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class RolesList(APIView):

    def post(self, request, company_pk, format=None):
        serializer = RolesSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def get(self, request, company_pk, format=None):
        queryset = Roles.objects.filter(company__id= company_pk)  
        serializer = RolesSerializer(queryset, many= True)
        return Response(serializer.data)

class MemberRoleDetail(APIView):
    def get_object(self, company_pk, member_id):
        try:
            return Members.objects.get(id = member_id, company__id = company_pk)
        except Members.DoesNotExist:
            raise Http404

    def put(self, request, company_pk, member_id, format=None):
        role = Roles.objects.get(id = request.data['role'])
        member = self.get_object(company_pk, member_id)
        member.role = role
        serializer = MembersRetrieveSerializer(member, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
