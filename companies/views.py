from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.response import Response

from django.http import Http404

from companies.serializers import MembersSerializer, MembersRetrieveSerializer, RolesSerializer
from companies.models import Members, Roles

class CompanyMembersList(APIView):
    def post(self, request, company_pk,format=None):
        serializer = MembersSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def get(self, request, company_pk, format=None):
        queryset = Members.objects.filter(company__id= company_pk)  
        serializer = MembersRetrieveSerializer(queryset, many= True)
        return Response(serializer.data)

class MemberDetails(APIView):
    def get_object(self, company_pk, member_id):
        try:
            return Members.objects.filter(id = member_id, company__id=company_pk)
        except Members.DoesNotExist:
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
        member = self.get_object(company_pk, member_id)
        serializer = MembersRetrieveSerializer(member, data = request.data)
        if serializer.is_valid():
            serializer.save()
            print serializer.data 
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

