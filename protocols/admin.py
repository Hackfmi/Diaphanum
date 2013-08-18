from django.contrib import admin
from .models import Protocol, Topic, Institution


class ProtocolAdmin(admin.ModelAdmin):
    list_display = ['number', 'start_time', 'get_topics', 'information', 'majority', 'current_majority', 'institution']

    list_display_links = ['number']

    list_filter = ['institution__name', 'topics']

    search_fields =['number', 'institution__name', 'topics__name', 'information']

admin.site.register(Institution)
admin.site.register(Topic)
admin.site.register(Protocol, ProtocolAdmin)
