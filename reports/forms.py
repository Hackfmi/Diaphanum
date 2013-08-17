from django import forms

from .models import Report


class ReportForm(forms.ModelForm):
    def save(self, *args, **kwargs):
        instance = super(ReportForm, self).save(commit=False)
        return instance.save(*args, **kwargs)

    class Meta:
        model = Report
        fields = ["addressed_to", "reported_from", "content", "created_at", "copies"]