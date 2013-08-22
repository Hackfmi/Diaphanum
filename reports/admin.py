# coding: utf-8
import reversion
from django.contrib import admin
from .models import Report, Copy


class ReportAdmin(reversion.VersionAdmin, admin.ModelAdmin):
    list_display = ('addressed_to', 'reported_from', 'signed_from', 'created_at')
    list_filter = ['created_at']
    search_fields = ['addressed_to', 'reported_from__username', 'content', 'signed_from']


class CopyAdmin(reversion.VersionAdmin, admin.ModelAdmin):
    list_display = ('copy_info', )
    history_latest_first = False


admin.site.register(Report, ReportAdmin)
admin.site.register(Copy, CopyAdmin)
