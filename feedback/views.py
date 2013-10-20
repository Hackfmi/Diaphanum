# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .forms import FeedbackForm


@permission_required('feedback.add_position')
def add(request):
    data = request.POST if request.POST else None
    feedback_form = FeedbackForm(data)
    if feedback_form.is_valid():
        feedback_form.save()
        return redirect('members:user-projects')
    return render(request, 'feedback/add_form.html', {'feedback_form': feedback_form})
