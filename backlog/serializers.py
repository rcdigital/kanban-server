from rest_framework import serializers
from backlog.models import Backlogs, Stories
from projects.serializers import ProjectSerializer

class BacklogSerializer (serializers.ModelSerializer):
    class Meta:
        model = Backlogs
        fields = ('name', 'project', 'hash_id',)

class BacklogSerializerRetrieve (serializers.ModelSerializer):
    project = ProjectSerializer(read_only = True)
    class Meta:
        model = Backlogs
        fields = ('name', 'project', 'hash_id', )

class StorySerializer (serializers.ModelSerializer):
    backlog = BacklogSerializer(read_only = True)
    class Meta:
        model = Stories
        fields = ('name', 'backlog', 'order', 'hash_id',)
