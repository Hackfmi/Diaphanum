from django.conf.urls import *
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Protocol, Institution
from .forms import ProtocolForm, TopicFormSet, AttendanceForm
from members.models import User
from hackfmi.utils import json_view


@permission_required('protocols.add_protocol', login_url='members:login')
def add(request):
    data = request.POST if request.POST else None
    protocol_form = ProtocolForm(data)
    formset = TopicFormSet(data, instance=request.session.get('protocol_in_creation', Protocol()))

    if protocol_form.is_valid():
        protocol = protocol_form.save()
        request.session['protocol_in_creation'] = formset.instance = protocol
        if formset.is_valid():
            formset.save()
            del request.session['protocol_in_creation']

    return render(request, 'protocols/add.html', locals())


def list_all_protocols(request):
    protocols = Protocol.objects.all()
    return render(request, 'protocols/list.html', locals())


@json_view
def search(request, name):
    institutions = Institution.objects.filter(name__icontains=name)

    json_data = [dict(name=institution.name, id=institution.id) for institution in institutions]

    return json_data


def listing(request, page):
    protocols_list = Protocol.objects.all()
    paginator = Paginator(protocols_list, 30)

    protocols = paginator.page(page)

    return render(request, 'protocols/listing.html', {"protocols": protocols})


def show_protocol(request, protocol_id):
    protocol = get_object_or_404(Protocol, id=protocol_id)
    return render(request, 'protocols/protocol.html', locals())


def protocols_by_institution(request, searched_institution):
    protocols = Protocol.objects.filter(institution=Institution.objects.filter(name=searched_institution))
    return render(request, 'protocols/listing.html', locals())


def protocols_by_date_range(request, start_date, end_date):
    protocols = Protocol.objects.filter(conducted_at__range=(start_date, end_date))
    return render(request, 'protocols/listing.html', locals())

@permission_required("protocols.change_institution")
def add_member_to_institution(request, institution_id, user_id):
    institution = get_object_or_404(Institution, id=institution_id)
    user = get_object_or_404(User, id=user_id)
    institution.members.add(user)
    return render(request, 'protocols/add_member.html', locals())

def show_members_of_institution(request, institution_id):
    institution = get_object_or_404(Institution, id=institution_id)
    members = institution.members
    return render(request, 'protocols/institution_members.html', locals())

def attendance(request):
    form = AttendanceForm(request.GET if request.GET else None)                                                                                                                                                       
    institutions = Institution.objects.all()

    if form.is_valid():
        institution = form.search()                                                                                                                                                                                                                                                                            
        members = institution.members.all()
        protocols = Protocol.objects.filter(institution=institution).all()
        for i, member in enumerate(members):
            for j, protocol in enumerate(protocols):
                if member in protocol.attendents.all():
                    attend[i][j] = 0
                elif member in protocol.absent.all():
                    attend[i][j] = 1
                else:
                    attend[i][j] = 2

    return render(request, 'protocols/attendance.html', locals())
