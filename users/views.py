from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.response import Response
from django.http import Http404

from users.models import KanbanUsers 
from users.serializers import UsersSerializer
from companies.serializers import CompaniesSerializer


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

class KanbanUserCompanies(APIView):

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
