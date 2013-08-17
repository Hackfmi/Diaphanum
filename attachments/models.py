from django.db import models

from datetime import datetime


class Attachment(models.Model):
    file_name = models.FileField(upload_to='attachments')

    def __unicode__(self):
        return unicode(self.file_name)
