from django.conf.urls import url
from companies import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^(?P<company_pk>[0-9]+)/members/$', views.CompanyMembersList.as_view()),
    url(r'^(?P<company_pk>[0-9]+)/member/(?P<member_id>[0-9]+)/$', views.MemberDetails.as_view()),
    url(r'^(?P<company_pk>[0-9]+)/member/(?P<member_id>[0-9]+)/role/$', views.MemberRoleDetail.as_view()),
    url(r'^(?P<company_pk>[0-9]+)/roles/$', views.RolesList.as_view()),
]

urlpatterns = format_suffix_patterns (urlpatterns)
