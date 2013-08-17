from datetime import datetime

from django.db import models
from members.models import Member


class Topic(models.Model):
    name = model.CharField(max_length=100, required=True)
    description = model.TextField()

class Protocol(models.Model):
    date = model.DateField(default=datetime.now)
    number = model.CharField(max_length=20, required=True)
    scheduled_time = model.TimeField(required=True)
    start_time = model.TimeField(required=True)
    quorum = PositiveIntegerField(required=True)
    absent = PositiveIntegerField(required=True)
    attendents = ManyToMany(Member)
    topics = ManyToMany(Topic)
    voted_for = PositiveIntegerField(required=True)
    voted_against = PositiveIntegerField(required=True)
    voted_abstain = PositiveIntegerField(required=True)
    information = TextField()

    def __unicode__(self):
        return self.number