# -*- encoding:utf-8 -*-
from datetime import datetime

from django.db import models


class Copy(models.Model):
    for_report = models.ForeignKey('Report', related_name='copies')
    about_topic = models.ManyToManyField('protocols.Topic')

    def copy_info(self):
        return '\n'.join(["""От протокол {},
                             до {},
                             по точка {}""".format(topic.protocol,
                                           topic.protocol.institution, topic)
                for topic in self.about_topic.all()])


class Report(models.Model):
    addressed_to = models.TextField()
    reported_from = models.ForeignKey('members.User')
    content = models.TextField()
    created_at = models.DateField(default=datetime.now)
    signed_from = models.CharField(max_length=64)

    def __unicode__(self):
        return self.addressed_to

    def get_copies(self):
        return "\n".join([c.name for c in self.copies.all()])
