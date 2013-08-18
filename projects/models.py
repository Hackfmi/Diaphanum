# -*- encoding:utf-8 -*-

from django.db import models

from members.models import Member
from attachments.models import Attachment


class Project(models.Model):
    STATUS = (
                ('unrevised', u'Неразгледан'),
                ('returned', u'Върнат за корекция'),
                ('pending', u'Предстои да бъде разгледан на СИС'),
                ('approved', u'Разгледан и одобрен на СИС'),
                ('rejected', u'Разгледан и неодобрен на СИС')
            )
    user = models.ForeignKey(Member)
    name = models.CharField(max_length=100)
    flp = models.ForeignKey(Member, related_name='flp')
    team = models.ManyToManyField(Member, related_name='team')
    description = models.TextField()
    targets = models.TextField()
    tasks = models.TextField()
    target_group = models.TextField()
    schedule = models.TextField()
    resources = models.TextField()
    finance_description = models.TextField()
    partners = models.TextField(blank=True, null=True)
    files = models.ManyToManyField(Attachment)
    status = models.CharField(max_length=50,
                             choices=STATUS,
                             default='unrevised')
    date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.name
