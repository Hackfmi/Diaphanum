from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

from .forms import ReportForm


def can_add_reports(user):
    return user.is_authenticated() and user.has_perm('reports.add_report')


@user_passes_test(can_add_reports)
def add_report(request):
    data = request.POST if request else None
    form = ReportForm(data)

    if form.is_valid():
        form.save()
    return render(request, 'reports/report.html', locals())
