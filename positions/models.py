# -*- coding: utf-8 -*-
from django.db import models
from datetime import date


class Position(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(default=date.today())
    content = models.TextField()

    def __unicode__(self):
        return self.title
