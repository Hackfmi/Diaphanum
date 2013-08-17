from django import forms

from .models import Protocol


class ProtocolForm(forms.ModelForm):
    class Meta:
        model = Protocol
        fields = (
            "number",
            "scheduled_time",
            "start_time",
            "quorum",
            "absent",
            "attendents",
            "topics",
            "voted_for",
            "voted_against",
            "voted_abstain",
            "information",)