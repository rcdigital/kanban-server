from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from backlog.serializers import BacklogSerializer, BacklogSerializerRetrieve, StorySerializer, StorySerializerPost
from backlog.models import Backlogs, Stories

class BacklogList(APIView):
    def post(self, request, project_id, format=None):
        serializer = BacklogSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def get(self, request, project_id, format=None):
        queryset = Backlogs.objects.filter(project__id= project_id)  
        serializer = BacklogSerializerRetrieve(queryset, many= True)
        return Response(serializer.data)

class BacklogDetails(APIView):
    def get_object(self, project_id, backlog_id):
        try:
            return Backlogs.objects.get(project = project_id, id = backlog_id)
        except Backlogs.DoesNotExist:
            raise Http404

    def get(self, request, project_id, backlog_id, format=None):
        backlog = self.get_object(project_id, backlog_id)  
        serializer = BacklogSerializerRetrieve(backlog , many= True)
        return Response(serializer.data)
    
    def put(self, request, project_id, backlog_id, format=None):
        backlog = self.get_object(project_id, backlog_id)
        serializer = BacklogSerializerRetrieve(backlog, data = request.data, many= False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, project_id, backlog_id, format=None):
        backlog = self.get_object(project_id, backlog_id)
        backlog.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class BacklogStories(APIView):
    def get(self, request, backlog_id, format=None):
        stories = Stories.objects.filter(backlog__id = backlog_id)
        serializer = StorySerializer(stories, many= True)
        return Response(serializer.data)

    def post(self, request, backlog_id, format=None):
        serializer = StorySerializerPost(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class StoryDetails(APIView):
    def get_object(self, backlog_id ,story_id):
        try:
            return Stories.objects.get(backlog__id = backlog_id, id = story_id)
        except Backlogs.DoesNotExist:
            raise Http404 

    def get(self, request, backlog_id, story_id, format=None):
        story = self.get_object(backlog_id, story_id)
        serializer = StorySerializer(story)
        return Response(serializer.data)

    def put(self, request, backlog_id, story_id, format = None):
        story = self.get_object(backlog_id, story_id)
        serializer = StorySerializerPost(story, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
