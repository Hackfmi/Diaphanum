import calendar
import reversion

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from members.models import User
from .models import Project
from .forms import ProjectForm, RestrictedProjectForm


@login_required
@reversion.create_revision()
def add_project(request):
    data = request.POST if request.POST else None
    form = ProjectForm(data, user=request.user)

    if form.is_valid():
        form.save()
        return redirect('members:user-projects')
    return render(request, 'projects/add.html', locals())


@reversion.create_revision()
def edit_project(request, project_id=None):
    project = get_object_or_404(Project, id=project_id)
    if request.user == project.user and (project.status == 'unrevised'
                                         or project.status == 'returned'):
        data = request.POST if request.POST else None
        form = ProjectForm(data=data, user=request.user, instance=project)
        if form.is_valid():
            form.save()
            return redirect('members:user-projects')
        return render(request, 'projects/edit.html', locals())
    else:
        return redirect('members:user-projects')


@permission_required('projects.change_project', login_url="members:user-projects")
def edit_status(request, project_id=None):
    project = get_object_or_404(Project, id=project_id)
    data = request.POST if request.POST else None
    form = RestrictedProjectForm(data=data, instance=project)
    if form.is_valid():
        project.save()
        return redirect('members:user-projects')
    return render(request, 'projects/edit_status.html', locals())


def projects_archive(request):
    unrevised = Project.objects.filter(status='unrevised')
    returned = Project.objects.filter(status='returned')
    pending = Project.objects.filter(status='pending')
    approved = Project.objects.filter(status='approved')
    rejected = Project.objects.filter(status='rejected')
    projects = Project.objects.order_by('-created_at')
    return render(request, 'projects/archive.html', locals())


def show_project(request, project_id):
    project_show = get_object_or_404(Project, id=project_id)
    if len(reversion.get_for_object(project_show)) > 1:
        old_versions = True
    return render(request, 'projects/show_project.html', locals())


def projects_year_month(request, year, month):
    projects = Project.objects.filter(created_at__year=year,
                                      created_at__month=month)
    month_name = _(calendar.month_name[int(month)])
    return render(request, 'projects/show_month_year.html', locals())


def show_project_versions(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    version_history = [ver for ver in reversion.get_for_object(project)]
    for ver in version_history:
        ver.team = [User.objects.get(id=mem) for mem in ver.field_dict['team']]
        ver.flp = User.objects.get(id=ver.field_dict['flp'])
        ver.user = User.objects.get(id=ver.field_dict['user'])
    return render(request, 'projects/previous_project_versions.html', locals())
