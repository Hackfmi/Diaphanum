from django import forms
from django.forms.models import inlineformset_factory
from django.shortcuts import get_object_or_404

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

    class Meta:
        model = Topic
        exclude = ('protocol', 'attachment')
        fields = (
            "name",
            "voted_for",
            "voted_against",
            "voted_abstain",
            "statement", )


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


class AttendanceForm(forms.Form):

    institution_id = forms.CharField(max_length=64, required=False)

    def search(self):
        institution_id = self.cleaned_data.get("institution_id")
        institution = get_object_or_404(Institution, id=institution_id)
        return institution