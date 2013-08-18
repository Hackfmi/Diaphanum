# coding: utf-8
from django.contrib import admin
from .models import Report

class ReportAdmin(admin.ModelAdmin):
    list_display = ('addressed_to', 'reported_from', 'content', 'signed_from', 'get_copies', 'created_at')
    list_filter = ['created_at']
    search_fields = ['addressed_to', 'reported_from', 'content', 'signed_from']

admin.site.register(Report, ReportAdmin)