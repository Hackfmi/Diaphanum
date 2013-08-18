from datetime import datetime

from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Protocol(models.Model):
    date = models.DateField(default=datetime.now)
    number = models.CharField(max_length=20)
    scheduled_time = models.TimeField()
    start_time = models.TimeField()
    quorum = models.PositiveIntegerField()
    absent = models.PositiveIntegerField()
    attendents = models.ManyToManyField('members.User', related_name='protocols')
    topics = models.ManyToManyField(Topic)
    voted_for = models.PositiveIntegerField()
    voted_against = models.PositiveIntegerField()
    voted_abstain = models.PositiveIntegerField()
    information = models.TextField()
    attachments = models.ManyToManyField('attachments.Attachment')

    def __unicode__(self):
        return self.number
