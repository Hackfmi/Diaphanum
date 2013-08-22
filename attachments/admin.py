import reversion
from django.contrib import admin

from .models import Attachment


class AttachmentAdmin(reversion.VersionAdmin, admin.ModelAdmin):
    list_display = ('document_', )


admin.site.register(Attachment, AttachmentAdmin)
