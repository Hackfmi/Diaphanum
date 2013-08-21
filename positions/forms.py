from django import forms
from .models import Position


class PositionForm(forms.ModelForm):
    def save(self, *args, **kwargs):
        instance = super(PositionForm, self).save(commit=False)
        return instance.save(*args, **kwargs)

    class Meta:
        model = Position
        fields = ('title', 'content',)
