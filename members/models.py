from django.db import models
from django.contrib.auth.models import AbstractUser


class Member(AbstractUser):
    faculty_number = models.CharField(max_length=8)


    def __unicode__(self):
        return self.username

    def attended_meetings(self):
        return self.protocols.count()
