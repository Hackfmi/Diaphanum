import reversion

from django.contrib import admin
from .models import Project


class ProjectAdmin(reversion.VersionAdmin, admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
