from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
from django.shortcuts import render

# from members.models import User
# from .models import Protocol, Topic
from .forms import ProtocolForm, InstitutionForm, TopicFormSet


@login_required
def add(request):
    data = request.POST if request.POST else None
    protocol_form = ProtocolForm(data)
    topic_form = TopicFormSet(data)
    institution_form = InstitutionForm(data)

    if protocol_form.is_valid() and topic_form.is_valid() and institution_form.is_valid():
        institution_form.save()
        protocol_form.save()
        topic_form.save()

    return render(request, 'protocols/add.html', locals())
