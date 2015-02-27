from rest_framework import serializers
from backlog.serializers import StorySerializer
from companies.serializers import MembersSerializer
from tasks.models import Tasks

class TaskSerializer (serializers.ModelSerializer):
    model = Tasks
    created_by = MembersSerializer(read_only = True)
    doing_by = MembersSerializer(read_only = True)
    story = StorySerializer(read_only = True)
    fields = ('name', 'story', 'estimate_time', 'finish_time', 'state', 'created_by', 'doing_by', 'hash_id',)
