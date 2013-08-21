# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('positions.views',
    url(r'^add/$', 'add', name='add'),
)