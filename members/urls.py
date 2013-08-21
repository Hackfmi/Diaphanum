from django.conf.urls import patterns, url
from django.contrib import auth

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login',{'template_name': 'members/login_form.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^search/(?P<name>.*)/$', 'members.views.search', name='search'),
    url(r'^archive/$', 'members.views.archive_student_council', name='archive_student_council'),
    url(r'^profile/$', 'members.views.user_projects', name='user-projects'),
)
