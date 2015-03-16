from django.conf.urls import url
from projects import views 
from backlog import views as backlogViews
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^(?P<project_id>[0-9]+)/$', views.ProjectDetails.as_view()),
    url(r'^(?P<project_id>[0-9]+)/backlogs/$', backlogViews.BacklogList.as_view()),
]

urlpatterns = format_suffix_patterns (urlpatterns)
