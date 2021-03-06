# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from django.core.mail import send_mail
from django.conf import settings

from .forms import FeedbackForm


def add(request):
    data = request.POST if request.POST else None

    if request.POST:
        form = FeedbackForm(data)
        if form.is_valid():
            form.save()
            feedback = form.instance
            name = feedback.name
            email = feedback.email
            information = feedback.information
            send_mail(u"Обратна връзка",
                    u"Подател: {} {} информация: {}".format(name, email, information),
                    "diaphanum.fmi@gmail.com",
                    ["diaphanum.fmi@gmail.com"])
            return redirect('members:user-projects')
        else:
            form.errors['captcha'] = "Грешен отговор"

    else:
        form = FeedbackForm()

    return render(request, 'feedback/add_form.html', {'feedback_form': form})
