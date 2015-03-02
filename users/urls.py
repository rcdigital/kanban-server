from django.conf.urls import url
from users import views
from users.models import KanbanUsers
from rest_framework.generics import ListCreateAPIView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^add$', views.add),
    url(r'^$', ListCreateAPIView.as_view(model=KanbanUsers), name='user-list'),
]


urlpatterns = format_suffix_patterns (urlpatterns)
