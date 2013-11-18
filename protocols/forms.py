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
