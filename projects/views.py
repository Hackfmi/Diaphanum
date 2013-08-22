from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect


from .models import Project
from .forms import ProjectForm, RestrictedProjectForm


@login_required
def add_project(request):
    data = request.POST if request.POST else None
    form = ProjectForm(data, user=request.user)

    if form.is_valid():
        form.save()
        return redirect('members:user-projects')
    else:
        return render(request, 'projects/add.html', locals())


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
    return render(request, 'projects/edit_status.html', locals())


def projects_archive(request):
    unrevised = Project.objects.filter(status='unrevised')
    returned = Project.objects.filter(status='returned')
    pending = Project.objects.filter(status='pending')
    approved = Project.objects.filter(status='approved')
    rejected = Project.objects.filter(status='rejected')
    return render(request, 'projects/archive.html', locals())


def show_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'projects/show_project.html', {'project_show' : project})
