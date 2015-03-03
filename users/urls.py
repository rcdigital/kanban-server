from django.conf.urls import url
from users import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.KanbanUserList.as_view()),
    url(r'(?P<pk>[0-9]+)/companies/', views.KanbanUserCompanies.as_view()),
]


urlpatterns = format_suffix_patterns (urlpatterns)
