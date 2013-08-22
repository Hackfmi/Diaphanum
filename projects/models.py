# -*- encoding:utf-8 -*-
from datetime import date
from django.db import models


class Project(models.Model):
    STATUS = (
        ('unrevised', u'Неразгледан'),
        ('returned', u'Върнат за корекция'),
        ('pending', u'Предстои да бъде разгледан на СИС'),
        ('approved', u'Разгледан и одобрен на СИС'),
        ('rejected', u'Разгледан и неодобрен на СИС'))

    user = models.ForeignKey('members.User', related_name='projects')
    name = models.CharField(max_length=100)
    flp = models.ForeignKey('members.User', related_name='flp')
    team = models.ManyToManyField('members.User', related_name='team')
    description = models.TextField()
    targets = models.TextField()
    tasks = models.TextField()
    target_group = models.TextField()
    schedule = models.TextField()
    resources = models.TextField()
    finance_description = models.TextField()
    partners = models.TextField(blank=True, null=True)
    files = models.ManyToManyField('attachments.Attachment', blank=True)
    status = models.CharField(max_length=50,
                              choices=STATUS,
                              default='unrevised')
    discussed_at = models.DateField(blank=True, null=True)
    attitute = models.TextField(blank=True, null=True)
    number = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateField(default=date.today())

    def __unicode__(self):
        return self.name
