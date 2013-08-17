from django.db import models


class Attachment(models.Model):
    file_name = models.FileField(upload_to='attachments')

    def __unicode__(self):
        return self.file_name
