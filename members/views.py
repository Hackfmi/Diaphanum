# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib.auth import views

from hackfmi.utils import json_view
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
        return redirect('members.views.homepage')
    else:
        return views.login(request, template_name='members/login_form.html')