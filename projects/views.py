from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import user_passes_test


from .models import Project
from .forms import ProjectForm, RestrictedProjectForm


def can_edit_projects(user):
    return user.is_authenticated() and user.has_perm('projects.change_project')


@login_required
def add_project(request):
    data = request.POST if request.POST else None
    form = ProjectForm(data, user=request.user)

    if form.is_valid():
        form.save()

    return render(request, 'projects/add.html', locals())


@login_required
def edit_project(request, project_id=None):
    project = get_object_or_404(Project, id=project_id)
    if can_edit_projects(request.user) or request.user == project.user:
        return render(request, 'projects/edit.html', locals())
    else:
        raise Http404


# @permissiion_required('edit_status')
@user_passes_test(can_edit_projects)
def edit_status(request, project_id=None):
    project = get_object_or_404(Project, id=project_id)
    data = request.POST if request.POST else None
    form = RestrictedProjectForm(data=data, instance=project)
    import ipdb; ipdb.set_trace()
    if form.is_valid():
        form.save()

    return render(request, 'projects/edit_status.html', locals())