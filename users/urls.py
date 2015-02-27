from django.conf.urls import url
from users import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.users),
]


urlpatterns = format_suffix_patterns (urlpatterns)
