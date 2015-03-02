from rest_framework import serializers
from users.models import KanbanUsers 

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = KanbanUsers 
        fields = ('id', 'name', 'email', 'thumb', 'companies')
