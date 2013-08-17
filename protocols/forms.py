from django import forms

from .models import Protocol


class ProtocolForm(forms.ModelForm):
    class Meta:
        model = Protocol
        fields = ["name", "description", "goals", "tasks"]