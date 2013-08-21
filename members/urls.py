from django.conf.urls import patterns, url
from django.contrib import auth

urlpatterns = patterns('members.views',
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^search/(?P<name>.*)/$', 'search', name='search'),
    url(r'^archive/$', 'archive_student_council', name='archive_student_council'),
    url(r'^profile/$', 'user_projects', name='user-projects'),
)
