from django.shortcuts import render
from django.http import HttpResponse

from .models import User


def homepage(request):
    return render(request, "index.html", {})


def search(request, name):
    members = User.objects.filter(first_name__icontains=name) or \
        User.objects.filter(last_name__icontains=name) or \
        User.objects.filter(username__icontains=name)

    json_data = [dict(
        id=member.id,
        full_name=' '.join([member.first_name, member.last_name]))
                for member in members]

    return HttpResponse(json_data, mimetype='application/json')
