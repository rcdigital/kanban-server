from django.conf.urls import url
from projects import views 
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^(?P<backlog_id>[0-9]+)/$', views.BacklogDetail.as_view()),
]

urlpatterns = format_suffix_patterns (urlpatterns)
