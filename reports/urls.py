from django.conf.urls import patterns, url


urlpatterns = patterns('reports.views',
    url(r'^add/$', 'add_report', name='add_report'),
)