from datetime import datetime

from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    attachment = models.ManyToManyField('attachments.Attachment')
    voted_for = models.PositiveIntegerField(blank=True, null=True)
    voted_against = models.PositiveIntegerField(blank=True, null=True)
    voted_abstain = models.PositiveIntegerField(blank=True, null=True)
    statement = models.TextField(blank=True, null=True)
    protocol = models.ForeignKey('Protocol', related_name='topics')

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
    excused = models.ManyToManyField('members.User', related_name='meetings_excused')
    absent = models.ManyToManyField('members.User', related_name='meetings_absent')
    attendents = models.ManyToManyField('members.User', related_name='meetings_attend')
    start_time = models.TimeField()
    additional = models.TextField(blank=True, null=True)
    quorum = models.PositiveIntegerField()
    majority = models.PositiveIntegerField()
    current_majority = models.PositiveIntegerField()
    information = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.number

    def get_topics(self):
        return "; ".join([topic.name for topic in self.topics.all()])

    def get_absent(self):
        return "; ".join([user.first_name + ' ' + user.last_name for user in self.absent.all()])
