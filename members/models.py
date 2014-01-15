from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    faculty_number = models.CharField(max_length=8)

    def __unicode__(self):
        return unicode(self.username)

    def attended_meetings(self):
        return self.meetings_attend.all()

    def absent_meetings(self):
        return self.meetings_absent.all()

    def excused_meetings(self):
    	return self.meetings_excused.all()
