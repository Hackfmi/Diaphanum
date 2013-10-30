from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
from django.views.generic import TemplateView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'members.views.homepage', name='homepage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^members/', include('members.urls', namespace='members')),
    url(r'^projects/', include('projects.urls', namespace='projects')),
    url(r'^protocols/', include('protocols.urls', namespace='protocols')),
    url(r'^reports/', include('reports.urls', namespace='reports')),
    url(r'^positions/', include('positions.urls', namespace='positions')),
    url(r'^feedback/', include('feedback.urls', namespace='feedback')),
    url(r'^captcha/', include('captcha.urls')),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),

    url(r'^404/$', TemplateView.as_view(template_name='404.html'), name='404'),
)
