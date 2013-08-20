from django.conf.urls import patterns, url


urlpatterns = patterns('projects.views',
    url(r'^add/$', 'add_project', name='add_project'),
    url(r'^edit/(?P<project_id>.*)/$', 'edit_project', name='edit_project'),
    url(r'^status/(?P<project_id>.*)/$', 'edit_status', name='edit_status'),
)
