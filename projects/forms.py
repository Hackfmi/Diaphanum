# coding: utf-8
from django import forms
from django.db.models import Q

from .models import Project
from members.models import User


class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(ProjectForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        instance = super(ProjectForm, self).save(commit=False)
        instance.user = self.user
        instance.flp = self.user
        instance.status = 'unrevised'
        instance.save(*args, **kwargs)
        self.save_m2m()
        return instance

    class Meta:
        model = Project
        fields = (
            'name',
            'team',
            'description',
            'targets',
            'tasks',
            'target_group',
            'schedule',
            'resources',
            'finance_description',
            'partners',
            )


class RestrictedProjectForm(forms.ModelForm):
    def save(self, *args, **kwargs):
        instance = super(RestrictedProjectForm, self).save(commit=False)
        return instance

    class Meta:
        model = Project
        exclude = (
            'name', 'team', 'description', 'targets', 'tasks', 'target_group',
            'schedule', 'resources', 'finance_description', 'partners',
            'flp', 'created_at', 'user',
            )

        fileds = (
            'status',
            'attitude', )


class SearchProjectForm(forms.Form):

    name = forms.CharField(max_length=100, required=False)
    status = forms.ChoiceField(choices=Project.STATUS, required=False)
    flp = forms.CharField(max_length=100, required=False)

    def search(self):
        name = self.cleaned_data.get("name")
        status = self.cleaned_data.get("status")
        creator = self.cleaned_data.get("flp")

        projects = Project.objects.all()

        if name:
            projects = projects.filter(name__icontains=name)

        if status:
            projects = projects.filter(status=status)

        if creator:
            names = creator.split(' ')
            projects = projects.filter(
                user__in=User.objects.filter(Q(first_name__in=names) | Q(last_name__in=names)))

        return projects

