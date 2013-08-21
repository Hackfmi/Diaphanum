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
        import ipdb; ipdb.set_trace()
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
            "absent",
            "attendents",
            "start_time",
            "additional",
            "quorum",
            "majority",
            "current_majority",
            "information", )
