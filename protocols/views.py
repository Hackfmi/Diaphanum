from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from members.models import User
from .models import Protocol, Topic
from .forms import ProtocolForm


@login_required
def add(request):
    data = request.POST if request else None
    form = ProtocolForm(data)

    #import ipdb; ipdb.set_trace()

    if form.is_valid():
        form.save()

    return render(request, 'add.html', locals())
