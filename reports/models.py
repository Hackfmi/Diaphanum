from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from members.models import Member
from protocols.models import Topic
from django.contrib.auth.models import User

class Reports(models.Model):
    
    addressed_to = models.TextField()
    reported_from = models.ForeignKey(Member)
    content = models.TextField()
    created_at= models.DateField(_("Date"), default=datetime.now())
    copies = models.ManyToManyField(Topic)
    
    def __unicode__(self):
        return self.addressed_to

