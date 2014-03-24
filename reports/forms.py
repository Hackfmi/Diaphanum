from django import forms
from django.forms.models import inlineformset_factory

from .models import Report, Copy


class CopyForm(forms.ModelForm):
    def save(self, *args, **kwargs):
        instance = super(CopyForm, self).save(commit=False)
        self.save_m2m()
        return instance

    class Meta:
        model = Copy
        fields = (
            "for_report",
            "about_topic", )


CopyFormSet = inlineformset_factory(Report, Copy, extra=1)


class ReportForm(forms.ModelForm):
    def save(self, *args, **kwargs):
        return super(ReportForm, self).save()

    class Meta:
        model = Report
        fields = ("addressed_to", "reported_from", "content", "signed_from", )
