from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin


from members import views
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', views.homepage, name='homepage'),
    # Examples:
    # url(r'^$', 'hackfmi.views.home', name='home'),
    # url(r'^hackfmi/', include('hackfmi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^protocols/add/$', 'protocols.views.add', name='add-protocol'),
    url(r'^projects/add/$', 'projects.views.add_project', name='add-project'),
    url(r'^reports/$', 'reports.views.add', name='add-report'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,}),)
