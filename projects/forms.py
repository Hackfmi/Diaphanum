from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(ProjectForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        instance = super(ProjectForm, self).save(commit=False)
        instance.user = self.user
        instance.flp = self.user
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
            'partners',)


class RestrictedProjectForm(forms.ModelForm):

    def save(self, *args, **kwargs):
        instance = super(RestrictedProjectForm, self).save(commit=False)
        return instance

    class Meta:
        model = Project
        fileds = (
            'status',
            'attitude', )