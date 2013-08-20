from django.conf.urls import patterns, url


urlpatterns = patterns('protocols.views',
    url(r'^archive/$', 'list_all_protocols', name='list_all_protocols'),
    url(r'^add/$', 'add', name='add_protocol'),
    url(r'^search/(?P<name>.*)/$', 'search', name='search'),
    url(r'^page/(?P<page>(\d)*)/$', 'listing', name='listing')
)
