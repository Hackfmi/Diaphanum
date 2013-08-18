# coding: utf-8
from django.contrib import admin
from .models import Report

class ReportAdmin(admin.ModelAdmin):
    #Определя кои полета да се показват в заявката за извлизачне на анкети
    list_display = ('addressed_to', 'reported_from', 'content', 'created_at', 'signed_from', 'get_copies')
    #Добавя поле за филтриране
    list_filter = ['created_at']
    #Добавя поле за търсене по полето от БД въпрос
    search_fields = ['addressed_to', 'reported_from', 'content', 'signed_from']

admin.site.register(Report, ReportAdmin)