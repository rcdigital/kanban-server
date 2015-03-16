from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kanban.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/users/', include('users.urls')),
    url(r'^api/company/', include('companies.urls')),
    url(r'^api/project/', include('projects.urls')),
)

