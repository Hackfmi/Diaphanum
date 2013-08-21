# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from django.http import HttpResponse
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required

from hackfmi.utils import json_view
from .models import User
from protocols.models import Protocol


def homepage(request):
    return render(request, "index.html", {})


@json_view
def search(request, name):
    members = User.objects.filter(first_name__icontains=name) or \
        User.objects.filter(last_name__icontains=name) or \
        User.objects.filter(username__icontains=name)

    json_data = [dict(
        id=member.id,
        faculty_number=member.faculty_number,
        full_name=' '.join([member.first_name, member.last_name]))
                for member in members]

    return json_data


def login(request):
    if request.user.is_authenticated():
        return redirect('members.views.homepage')
    else:
        return views.login(request, template_name='members/login_form.html')


def archive_student_council(request):
    protocols = Protocol.objects.all().order_by('-conducted_at')
    return render(request, 'members/archive.html', locals())

def logout(request):
    #При auth.views.logout дава грешка, че не може да намери logout!
    views.logout(request)
    return redirect('members.views.homepage')
    # if not request.user.is_superuser:
    #     auth.logout(request)
    #     return redirect('members.views.homepage')
    # else:
    #     return HttpResponseRedirect('/admin/logout/')


@login_required
def user_projects(request, **kwargs):
    # import ipdb; ipdb.set_trace()
    projects = request.user.projects.all()
    return render(request, 'members/profile.html', locals())
