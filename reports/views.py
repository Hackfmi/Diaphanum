from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.core.paginator import Paginator

from .forms import ReportForm
from .models import Report


def can_add_reports(user):
    return user.is_authenticated() and user.has_perm('reports.add_report')


@user_passes_test(can_add_reports)
def add_report(request):
    data = request.POST if request else None
    form = ReportForm(data)

    if form.is_valid():
        form.save()
    return render(request, 'reports/report.html', locals())


def listing(request, page):
    reports_list = Report.objects.all()
    paginator = Paginator(reports_list, 30)

    reports = paginator.page(page)

    return render(request, 'reports/listing.html', {"reports": reports})
