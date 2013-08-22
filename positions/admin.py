import reversion

from django.contrib import admin
from .models import Position


class PositionAdminIndex(reversion.VersionAdmin, admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']
    search_fields = ['title', 'content']

admin.site.register(Position, PositionAdminIndex)
