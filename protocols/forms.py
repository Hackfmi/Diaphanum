from datetime import datetime

from django import forms
from django.forms.models import inlineformset_factory

from .models import Protocol, Institution, Topic


class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ("name", )


class TopicForm(forms.ModelForm):
    def save(self, *args, **kwargs):
        instance = super(TopicForm, self).save(commit=False)
        self.protocol = Protocol.objects.get(kwargs['protocol'])
        self.save_m2m()
        return instance

    def clean(self):
        cleaned_data = super(TopicForm, self).clean()
        files = self.files.values()
        if self.instance.pk:
            already_attached = self.instance.files.all()
        else:
            already_attached = []
        if len(files) > 0:
            cleaned_data['files'] = [Attachment.objects.create(file_name=file) for file in files]
            for file in files:
                if file._size > FILE_UPLOAD_MAX_MEMORY_SIZE:
                    raise forms.ValidationError("This file is bigger than 20MB")
        elif 'files' in self._errors:
            del self._errors['files']
        if len(files) + len(already_attached) > 5:
            raise forms.ValidationError("You are trying to upload more than 5 files")
        cleaned_data['files'] = list(cleaned_data['files']) + list(already_attached)
        return cleaned_data

    class Meta:
        model = Topic
        exclude = ('protocol')
        fields = (
            "name",
            "voted_for",
            "voted_against",
            "voted_abstain",
            "statement",
            "attachment",
        )


TopicFormSet = inlineformset_factory(Protocol, Topic, extra=2)


class ProtocolForm(forms.ModelForm):
    def save(self, *args, **kwargs):
        return super(ProtocolForm, self).save()

    class Meta:
        model = Protocol
        fields = (
            "institution",
            "number",
            "scheduled_time",
            "excused",
            "absent",
            "attendents",
            "start_time",
            "additional",
            "quorum",
            "majority",
            "current_majority",
            "voted_for",
            "voted_against",
            "voted_abstain",
            "information", )


class SearchProtocolForm(forms.Form):

    institution = forms.CharField(max_length=64, required=False)
    start_date = forms.DateField(required=False, initial=Protocol.get_oldest_protocol_date())
    end_date = forms.DateField(required=False, initial=datetime.now)

    def search(self):
        institution = self.cleaned_data.get("institution")
        start_date = self.cleaned_data.get("start_date")
        end_date = self.cleaned_data.get("end_date")

        protocols = Protocol.objects.all()

        if institution:
            protocols = protocols.filter(institution__in=Institution.objects.filter(name=institution))

        protocols.filter(conducted_at__range=(start_date, end_date))

        return protocols
