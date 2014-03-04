# coding: utf-8
from django import forms
from django.db.models import Q
from django.conf import settings

from attachments.models import Attachment
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

    def clean(self):
        cleaned_data = super(ProjectForm, self).clean()
        files = self.files.values()
        if self.instance.pk:
            already_attached = self.instance.files.all()
        else:
            already_attached = []
        if len(files) > 0:
            cleaned_data['files'] = [Attachment.objects.create(file_name=file) for file in files]
            for file in files:
                if file._size > settings.FILE_UPLOAD_MAX_MEMORY_SIZE:
                    raise forms.ValidationError("This file is bigger than 20MB")
        elif 'files' in self._errors:
            del self._errors['files']
        if len(files) + len(already_attached) > 15:
            raise forms.ValidationError("You are trying to upload more than 15 files")
        cleaned_data['files'] = list(cleaned_data['files']) + list(already_attached)
        return cleaned_data

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
            'files',)


class RestrictedProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RestrictedProjectForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs = {'class': "form-control"}

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
            'discussed_at',
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

