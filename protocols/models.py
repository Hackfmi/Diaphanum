from datetime import datetime, date

from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=100)
    files = models.ManyToManyField('attachments.Attachment', blank=True)
    voted_for = models.PositiveIntegerField(blank=True, default=0)
    voted_against = models.PositiveIntegerField(blank=True, default=0)
    voted_abstain = models.PositiveIntegerField(blank=True, default=0)
    statement = models.TextField(blank=True, null=True)
    protocol = models.ForeignKey('Protocol', related_name='topics')

    def __unicode__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=64)
    members = models.ManyToManyField('members.User', blank=True)

    def __unicode__(self):
        return self.name


class Protocol(models.Model):
    conducted_at = models.DateField(default=datetime.now)
    institution = models.ForeignKey(Institution)
    number = models.CharField(max_length=20, unique=True)
    scheduled_time = models.TimeField()
    excused = models.ManyToManyField('members.User', related_name='meetings_excused', blank=True)
    absent = models.ManyToManyField('members.User', related_name='meetings_absent', blank=True)
    attendents = models.ManyToManyField('members.User', related_name='meetings_attend')
    start_time = models.TimeField()
    additional = models.TextField(blank=True, null=True)
    quorum = models.PositiveIntegerField()
    majority = models.PositiveIntegerField()
    current_majority = models.PositiveIntegerField()
    voted_for = models.PositiveIntegerField(blank=True, default=0)
    voted_against = models.PositiveIntegerField(blank=True, default=0)
    voted_abstain = models.PositiveIntegerField(blank=True, default=0)
    information = models.TextField(blank=True, null=True)
    files = models.ManyToManyField('attachments.Attachment', blank=True)

    def __unicode__(self):
        return self.number

    def get_topics(self):
        return "; ".join([topic.name for topic in self.topics.all()])

    def get_absent(self):
        return "; ".join([user.first_name + ' ' + user.last_name for user in self.absent.all()])

    @classmethod
    def get_oldest_protocol_date(cls):
        try:
            return cls.objects.order_by('conducted_at')[0].conducted_at
        except IndexError:
            return date.today()

