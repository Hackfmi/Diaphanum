from django import forms
from django.conf import settings
from django.forms.models import inlineformset_factory, BaseInlineFormSet

from .models import Protocol, Institution, Topic
from attachments.models import Attachment


class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ("name", )


class TopicForm(forms.ModelForm):
    # def clean(self):
    #     import ipdb; ipdb.set_trace()
    #     cleaned_data = self.clean()
    #     files = [file for name, file in self.files.items()]
    #     import ipdb; ipdb.set_trace()
    #     if self.instance.pk:
    #         already_attached = self.instance.files.all()
    #     else:
    #         already_attached = []
    #     if len(files) > 0:
    #         cleaned_data['files'] = [Attachment.objects.create(file_name=file) for file in files]
    #         for file in files:
    #             if file._size > settings.FILE_UPLOAD_MAX_MEMORY_SIZE:
    #                 raise forms.ValidationError("This file is bigger than 20MB")
    #     elif 'files' in self._errors:
    #         del self._errors['files']
    #     if len(files) + len(already_attached) > 5:
    #         raise forms.ValidationError("You are trying to upload more than 5 files")
    #     cleaned_data['files'] = list(cleaned_data['files']) + list(already_attached)
    #     return cleaned_data

    class Meta:
        model = Topic
        exclude = ('protocol', )
        fields = (
            "name",
            "voted_for",
            "voted_against",
            "voted_abstain",
            "statement",
            "files",
        )

class BaseTopicFormSet(BaseInlineFormSet):
    def clean(self):
        for i, form in enumerate(self.forms):
        #     import ipdb; ipdb.set_trace()
        #     form.cleaned_data = form.clean()
            #     import ipdb; ipdb.set_trace()
            cleaned_data = form.clean()
            files = [file for name, file in self.files.items() if name.startswith('topics-{}'.format(i))]
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
            if len(files) + len(already_attached) > 5:
                raise forms.ValidationError("You are trying to upload more than 5 files")
            cleaned_data['files'] = list(cleaned_data['files']) + list(already_attached)
            form.cleaned_data = cleaned_data

TopicFormSet = inlineformset_factory(Protocol, Topic, formset=BaseTopicFormSet, extra=2)


class ProtocolForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(ProtocolForm, self).clean()
        files = [file for name, file in self.files.items() if not name.startswith('topics')]

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
        if len(files) + len(already_attached) > 5:
            raise forms.ValidationError("You are trying to upload more than 5 files")
        cleaned_data['files'] = list(cleaned_data['files']) + list(already_attached)
        return cleaned_data

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
            "information",
            "files", )
