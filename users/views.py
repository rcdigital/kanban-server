from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import KanbanUsers 
from users.serializers import UsersSerializer


@api_view(['GET', 'POST'])
def users(request, format= None):

    if request.method == 'GET':
        users = KanbanUsers.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsersSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
