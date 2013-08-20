from django.conf.urls import patterns, url


urlpatterns = patterns('members.views',
    url(r'^login/$', 'login', name='login'),
    url(r'^search/(?P<name>.*)/$', 'search', name='search'),
)
