from django.db import models

from members.models import Member
from attachments.models import Attachment


class Project(models.Model):
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
    partners = models.TextField()
    files = models.ManyToManyField(Attachment)

    def __unicode__(self):
        return self.name
