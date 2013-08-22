# coding: utf-8
from django.contrib import admin
from .models import Report, Copy


class ReportAdmin(admin.ModelAdmin):
    list_display = ('addressed_to', 'reported_from', 'signed_from', 'created_at')
    list_filter = ['created_at']
    search_fields = ['addressed_to', 'reported_from__username', 'content', 'signed_from']


class CopyAdmin(admin.ModelAdmin):
    list_display = ('copy_info', )


admin.site.register(Report, ReportAdmin)
admin.site.register(Copy, CopyAdmin)
