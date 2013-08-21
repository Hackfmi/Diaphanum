from django.conf.urls import patterns, url


urlpatterns = patterns('projects.views',
    url(r'^add/$', 'add_project', name='add_project'),
    url(r'^edit/(?P<project_id>\d+)/$', 'edit_project', name='edit_project'),
    url(r'^edit_status/(?P<project_id>\d+)/$', 'edit_status', name='edit_status'),
    url(r'^status/(?P<project_id>\d+)/$', 'edit_status', name='edit_status'),
    url(r'^archive/$', 'projects_archive', name='projects_archive'),
    url(r'^archive/review/(?P<project_id>\d+)/$', 'show_project', name='show-project'),
)
