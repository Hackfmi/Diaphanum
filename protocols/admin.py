from django.contrib import admin
from .models import Protocol, Topic, Institution


class ProtocolAdmin(admin.ModelAdmin):
    list_display = ['number', 'start_time', 'get_topics', 'information', 'majority', 'current_majority', 'get_absent']

    list_display_links = ['number']

    list_filter = ['topics']

    search_fields =['number', 'information', 'topics__name', 'topics__description']

admin.site.register(Institution)
admin.site.register(Topic)
admin.site.register(Protocol, ProtocolAdmin)
