from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.response import Response

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
    def get(self, request, company_pk, member_id, format=None):
        queryset = Members.objects.filter(company__id= company_pk, member__id= member_id)  
        serializer = MembersRetrieveSerializer(queryset, many= True)
        return Response(serializer.data)

class RolesList(APIView):

    def post(self, request, company_pk, format=None):
        serializer = RolesSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def get(self, request, company_pk, format=None):
        queryset = Roles.objects.filter(company__id= company_pk)  
        print company_pk
        serializer = RolesSerializer(queryset, many= True)
        return Response(serializer.data)
