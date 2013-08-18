from django.contrib import admin
from .models import Protocol, Topic


# class ProtocolAdmin(admin.ModelAdmin):
#     list_display = ['number', 'date', 'scheduled_time', 'start_time', 'get_topics', 'information', 'voted_for',
#                     'voted_against', 'voted_abstain']
#
#     list_display_links = ['number']
#
#     list_filter = ['topics', 'date']
#
#     search_fields =['number', 'information', 'topics__name', 'topics__description']


admin.site.register(Topic)
admin.site.register(Protocol)
