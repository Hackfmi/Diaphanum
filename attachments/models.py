from django.db import models


class Attachment(models.Model):
    file_name = models.FileField(upload_to='attachments')

    def __unicode__(self):
        return unicode(self.file_name)

    def document_(self):
        return format(str(self.file_name).split('/')[-1])

