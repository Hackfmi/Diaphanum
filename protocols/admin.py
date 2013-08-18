from django.contrib import admin
from .models import Protocol, Topic, Institution


admin.site.register(Institution)
admin.site.register(Topic)
admin.site.register(Protocol)
