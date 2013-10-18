from django.conf.urls import patterns, url


urlpatterns = patterns('projects.views',
    url(r'^add/$', 'add_project', name='add-project'),
    url(r'^edit/(?P<project_id>\d+)/$', 'edit_project', name='edit-project'),
    url(r'^edit/(?P<project_id>\d+)/files/delete/(?P<file_id>\d+)/$', 'remove_file', name='remove-file'),
    url(r'^edit_status/(?P<project_id>\d+)/$', 'edit_status', name='edit-status'),
    url(r'^archive/$', 'projects_archive', name='projects-archive'),
    url(r'^archive/review/(?P<project_id>\d+)/$', 'show_project', name='show-project'),
    url(r'^archive/review/versions/(?P<project_id>\d+)/$', 'show_project_versions', name='show-project-versions'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{,2})/$', 'projects_year_month', name='projects-year-month'),
    url(r'^confirm/(?P<confirmation>.*)/$', 'confirm_participation', name='confirm-participation')
)
