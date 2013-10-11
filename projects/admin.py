import reversion

from django.contrib import admin
from .models import Project


class ProjectAdmin(reversion.VersionAdmin, admin.ModelAdmin):
    filter_horizontal = ('files', 'team', 'participating')


admin.site.register(Project, ProjectAdmin)
