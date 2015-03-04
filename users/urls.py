from django.conf.urls import url
from users import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.KanbanUserList.as_view()),
    url(r'(?P<pk>[0-9]+)/$', views.KanbanUserDetail.as_view()),
    url(r'(?P<pk>[0-9]+)/companies/$', views.KanbanUserCompaniesList.as_view()),
    url(r'(?P<pk>[0-9]+)/companies/(?P<company_id>[0-9]+)/$', views.KanbanUserCompaniesDetail.as_view()),
]


urlpatterns = format_suffix_patterns (urlpatterns)
