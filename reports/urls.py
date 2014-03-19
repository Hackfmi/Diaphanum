from django.conf.urls import patterns, url


urlpatterns = patterns('reports.views',
    url(r'^add/$', 'add_report', name='add-report'),
    url(r'^archive/(?P<page>.*)/$', 'listing', name='listing'),
    url(r'^show/(?P<id>.*)/$', 'show', name='show'),

)
