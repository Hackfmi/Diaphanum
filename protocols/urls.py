from django.conf.urls import patterns, url


urlpatterns = patterns('protocols.views',
    url(r'^archive/review/(?P<protocol_number>.+)/$', 'show_protocol', name='show-protocol'),
    url(r'^archive/(?P<page>.*)/$', 'listing', name='listing'),
    url(r'^add/$', 'add', name='add_protocol'),
    url(r'^search/(?P<name>.*)/$', 'search', name='search'),
)
