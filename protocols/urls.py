from django.conf.urls import patterns, url


urlpatterns = patterns('protocols.views',
    url(r'^archive/review/(?P<protocol_id>.+)/$', 'show_protocol', name='show-protocol'),
    url(r'^archive/(?P<page>.*)/$', 'listing', name='listing'),
    url(r'^add/$', 'add', name='add-protocol'),
    url(r'^institution/members/(?P<institution_id>(\d)*)/$', 'show_members_of_institution', name='show-members-of-institution'),
    url(r'^institution/add_member/(?P<institution_id>(\d)*)/(?P<user_id>(\d)*)/$', 'add_member_to_institution', name='add-member-to-institution'),
    url(r'^institution/(?P<searched_institution>.*)/$', 'protocols_by_institution', name='protocols-by-institution'),
    url(r'^search/(?P<start_date>.*)/(?P<end_date>.*)/$', 'protocols_by_date_range', name='protocols-by-date-range'),
    url(r'^search/(?P<name>.*)/$', 'search', name='search'),
    url(r'^page/(?P<page>(\d)*)/$', 'listing', name='listing'),
    url(r'^attendance/$', 'attendance', name='attendance'),

)
