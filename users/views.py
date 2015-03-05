from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.response import Response

from django.http import Http404

from users.models import KanbanUsers 
from users.serializers import UsersSerializer, UsersDetailSerializer
from companies.serializers import CompaniesSerializer, CompaniesRetrieveSerializer, CompaniesTestSerializer
from companies.models import Companies


class KanbanUserList(APIView):

    def get(self, request, format=None):
        queryset = KanbanUsers.objects.all()
        serializer = UsersSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UsersSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KanbanUserDetail(APIView):
    def get_object(self, pk):
        try:
            return KanbanUsers.objects.get(id = pk)
        except KanbanUsers.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UsersDetailSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format= None):
        user = self.get_object(pk)
        user.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UsersSerializer(user)
        return Response(serializer.data)

class KanbanUserCompaniesList(APIView):

    def get(self, request, pk, format=None):
        queryset = KanbanUsers.objects.get(id = pk)
        serializer = UsersSerializer(queryset)
        return Response(serializer.data['companies'])

    def post(self, request, pk, format=None):
        serializer = CompaniesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KanbanUserCompaniesDetail(APIView):
    def get_object(self, pk, company_id):
        try:
            return Companies.objects.get(id = company_id, owner__id=pk)
        except Companies.DoesNotExist:
            raise Http404

    def put(self, request, pk, company_id, format=None):
        company = self.get_object(pk, company_id)
        serializer = CompaniesTestSerializer(company, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, company_id, format= None):
        company = self.get_object(pk, company_id)
        company.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    def get(self, request, pk, company_id, format=None):
        company = self.get_object(pk, company_id)
        serializer = CompaniesRetrieveSerializer(company)
        return Response(serializer.data)
