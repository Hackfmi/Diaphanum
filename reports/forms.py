from django import forms

from .models import Reports


class ReportsForm(forms.ModelForm):
    def save(self, *args, **kwargs):
        instance = super(ReportsForm, self).save(commit=False)
        return instance.save(*args, **kwargs)

    class Meta:
        model = Reports
        fields = ["addressed_to", "reported_from", "content", "created_at", "copies"]