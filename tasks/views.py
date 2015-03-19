from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.response import Response

from django.http import Http404

from tasks.serializers import TaskSerializer, TasksGroupBySerializer, TaskPostSerializer
from tasks.models import Tasks
from django.db.models import Count


from backlog.serializers import StorySerializer
from backlog.models import Stories

class TasksList(APIView):
    def get(self, request, backlog_id, story_id, format=None):
        doing = Tasks.objects.filter(story__id = story_id, status='doing')
        todo = Tasks.objects.filter(story__id = story_id, status='todo')
        done = Tasks.objects.filter(story__id = story_id, status='done')
        todo_serializer = TasksGroupBySerializer(todo, many= True)
        doing_serializer = TasksGroupBySerializer(doing, many= True)
        done_serializer = TasksGroupBySerializer(done, many= True)
        story = Stories.objects.get(id = story_id)
        story_serializer = StorySerializer(story)
        
        tasks_list = {'story': story_serializer.data ,'todo': todo_serializer.data, 'doing': doing_serializer.data, 'done': done_serializer.data}
        print tasks_list
        return Response(tasks_list)

    def post(self, request, backlog_id, story_id, format=None):
        serializer = TaskPostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class TaskDetails(APIView):
    def get_object(self, task_id, format=None):
        try:
            return Tasks.objects.get(id = task_id)
        except Tasks.DoesNotExist:
            return Http404

    def put(self, request, backlog_id, story_id, task_id):
        task = self.get_object(task_id)
        serializer = TaskPostSerializer(task, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def get(self, request, backlog_id, story_id, task_id):
        task = self.get_object(task_id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def delete(self, request, backlog_id, story_id, task_id):
        task = self.get_object(task_id)
        task.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
