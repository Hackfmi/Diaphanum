from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from members.models import User
from .models import Protocol, Topic
from .forms import ProtocolForm, TopicForm, InstitutionForm, TopicFormSet


@login_required
def add(request):
    data = request.POST if request.POST else None
    form = ProtocolForm(data)
    formset = TopicFormSet(data)
    form_institution = InstitutionForm(data)

    if form.is_valid() and formset.is_valid() and form_institution.is_valid():
        form_institution.save()
        form.save()
        formset.save()

    return render(request, 'protocols/add.html', locals())
