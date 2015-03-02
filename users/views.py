from rest_framework import status, renderers, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import KanbanUsers 
from users.serializers import UsersSerializer


class UserList(generics.ListCreateAPIView):
    queryset = KanbanUsers.objects.all()
    serializer_class = UsersSerializer
    def list(self, request):
        queryset = self.get_queryset()
        serializer = UsersSerializer(queryset, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def add(request, format=None):
    if request.method == 'POST':
        serializer = UsersSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

    return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)


class UserCompanies(generics.GenericAPIView):
    queryset = KanbanUsers.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer, )

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        return Response(user.companies)
