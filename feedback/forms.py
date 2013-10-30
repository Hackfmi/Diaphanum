from django import forms
from captcha.fields import CaptchaField

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    captcha = CaptchaField()

    def save(self, *args, **kwargs):
        instance = super(FeedbackForm, self).save(commit=False)
        return instance.save(*args, **kwargs)

    class Meta:
        model = Feedback
        fields = ('name', 'email', 'information',)
