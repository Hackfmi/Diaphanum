from datetime import datetime

from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    attachment = models.ManyToManyField('attachments.Attachment')
    voted_for = models.PositiveIntegerField()
    voted_against = models.PositiveIntegerField()
    voted_abstain = models.PositiveIntegerField()
    statement = models.TextField()

    def __unicode__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class Protocol(models.Model):
    conducted_at = models.DateField(default=datetime.now)
    institution = models.ForeignKey(Institution)
    number = models.CharField(max_length=20, unique=True)
    scheduled_time = models.TimeField()
    absent = models.ManyToManyField('members.User', related_name='meetings_absent')
    attendents = models.ManyToManyField('members.User', related_name='meetings_attend')
    start_time = models.TimeField()
    additional = models.TextField(blank=True, null=True)
    quorum = models.PositiveIntegerField()
    majority = models.PositiveIntegerField()
    current_majority = models.PositiveIntegerField()
    topics = models.ManyToManyField(Topic)
    information = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.number

    def get_topics(self):
        return "; ".join([t.name for t in self.topics.all()])