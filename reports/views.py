from django.shortcuts import render

from .forms import ReportForm


def add_report(request):
    data = request.POST if request else None
    form = ReportForm(data)

    if form.is_valid():
        form.save()
    return render(request, 'reports/report.html', locals())
