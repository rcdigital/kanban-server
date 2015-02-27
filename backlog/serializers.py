from rest_framework import serializers
from backlog.models import Backlog, Stories
from projects.models import ProjectSerializer

class BacklogSerializer (serializers.ModelSerializer):
    model = Backlog
    project = ProjectSerializer(read_only = True)
    fields = ('name', 'project', 'hash_id', )

class StorySerializer (serializers.ModelSerializer):
    model = Stories
    backlog = BacklogSerializer(read_only = True)
    fields = ('name', 'backlog', 'order', 'hash_id',)
