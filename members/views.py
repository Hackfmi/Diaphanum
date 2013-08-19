# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib import auth

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
    data = request.POST if request else None
    form = LoginForm(data)

    if request.POST:
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('members.views.homepage')
                else:
                    pass
                    # Return a 'disabled account' error message
            else:
                pass
                # Return an 'invalid login' error message
    return render(request, 'members/login_form.html', locals())
