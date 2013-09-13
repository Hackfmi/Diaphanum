from django.conf.urls import patterns, url


urlpatterns = patterns('protocols.views',
    url(r'^archive/review/(?P<protocol_id>.+)/$', 'show_protocol', name='show-protocol'),
    url(r'^archive/(?P<page>.*)/$', 'listing', name='listing'),
    url(r'^add/$', 'add', name='add-protocol'),
    url(r'^institution/(?P<searched_institution>.*)/$', 'protocols_by_institution', name='protocols-by-institution'),
    url(r'^search/(?P<name>.*)/$', 'search', name='search'),
    url(r'^page/(?P<page>(\d)*)/$', 'listing', name='listing'),
)
