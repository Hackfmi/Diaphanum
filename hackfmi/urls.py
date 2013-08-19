from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import TemplateView


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
    url(r'^login/$', 'members.views.login', name='login'),
    url(r'^search/(?P<name>.*)/$', 'members.views.search', name='search'),
    url(r'^projects/add/$', 'projects.views.add_project', name='add-project'),
    url(r'^projects/edit/(?P<project_id>.*)$', 'projects.views.edit_project', name='edit-project'),
    url(r'^projects/status/(?P<project_id>.*)$', 'projects.views.edit_status', name='edit-status'),
    url(r'^protocols/$', 'protocols.views.list_all_protocols', name='list_protocols'),
    url(r'^protocols/add/$', 'protocols.views.add', name='add-protocol'),
    url(r'^reports/add/$', 'reports.views.add_report', name='add-report'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
    url(r'^404/$', TemplateView.as_view(template_name='404.html'), name='404'),
)
