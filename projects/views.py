from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Project
from .forms import ProjectForm


@login_required
def add_project(request):
    data = request.POST if request.POST else None
    form = ProjectForm(data, user=request.user)

    if form.is_valid():
        form.save()

    return render(request, 'projects/add.html', locals())



