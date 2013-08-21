from django.shortcuts import render, get_object_or_404
from django.conf.urls import *
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator

from .models import Protocol, Institution
from .forms import ProtocolForm, TopicFormSet
from hackfmi.utils import json_view



def can_add_protocols(user):
    return user.is_authenticated() and user.has_perm('protocols.add_protocol')


@user_passes_test(can_add_protocols)
def add(request):
    data = request.POST if request.POST else None
    protocol_form = ProtocolForm(data)
    topic_form = TopicFormSet(data)

    if protocol_form.is_valid() and topic_form.is_valid():
        protocol_form.save()
        topic_form.save()

    return render(request, 'protocols/add.html', locals())


def list_all_protocols(request):
    protocols = Protocol.objects.all()
    return render(request, 'protocols/list.html', locals())


@json_view
def search(request, name):
    institutions = Institution.objects.filter(name__icontains=name)

    json_data = [dict(name=institution.name) for institution in institutions]

    return json_data


def listing(request, page):
    protocols_list = Protocol.objects.all()
    paginator = Paginator(protocols_list, 30)

    protocols = paginator.page(page)

    return render(request, 'protocols/listing.html', {"protocols": protocols})


def show_protocol(request, protocol_number):
    protocol = get_object_or_404(Protocol, id=protocol_number)
    return render(request, 'protocols/show_protocol.html', locals())
