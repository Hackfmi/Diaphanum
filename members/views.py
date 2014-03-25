# -*- coding: utf-8 -*-
from django.contrib.auth import views, authenticate
from django.contrib.auth import login as original_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from hackfmi.utils import json_view
from protocols.models import Protocol
from projects.models import Project
from .models import User


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
        return redirect('homepage')
    else:
        return views.login(request, template_name='members/login_form.html')


def archive_student_council(request):
    protocols = Protocol.objects.all().order_by('-conducted_at')
    return render(request, 'members/archive.html', locals())


def logout(request):
    views.logout(request)
    return redirect('homepage')


@login_required
def user_projects(request, **kwargs):
    projects = request.user.projects.all()
    all_projects = Project.objects.all()
    is_project_coordinator = request.user.has_perm('projects.change_project')
    can_add_protocols = request.user.has_perm('protocols.add_protocol')
    can_add_reports = request.user.has_perm('reports.add_report')
    return render(request, 'members/profile.html', locals())
