from django.conf.urls import patterns, url


urlpatterns = patterns('protocols.views',
    url(r'^archive/$', 'list_all_protocols', name='list_all_protocols'),
    url(r'^add/$', 'add', name='add_protocol'),
)
