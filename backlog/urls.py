from django.conf.urls import url
from backlog import views 
from tasks import views as tasksViews 
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^(?P<backlog_id>[0-9]+)/$', views.BacklogDetails.as_view()),
    url(r'^(?P<backlog_id>[0-9]+)/stories/$', views.BacklogStories.as_view()),
    url(r'^(?P<backlog_id>[0-9]+)/story/(?P<story_id>[0-9]+)/$', views.StoryDetails.as_view()),
    url(r'^(?P<backlog_id>[0-9]+)/story/(?P<story_id>[0-9]+)/tasks/$', tasksViews.TasksList.as_view()),
    url(r'^(?P<backlog_id>[0-9]+)/story/(?P<story_id>[0-9]+)/task/(?P<task_id>[0-9]+)/data/$', tasksViews.TaskDetails.as_view()),
]

urlpatterns = format_suffix_patterns (urlpatterns)
