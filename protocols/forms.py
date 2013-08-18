from django import forms

from .models import Protocol


class ProtocolForm(forms.ModelForm):
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
            "topics",
            "information", )
