from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.shortcuts import render

from .forms import ReportForm, CopyFormSet
from .models import Report


@permission_required('reports.add_report', login_url='members:login')
def add_report(request):
    data = request.POST if request else None
    report_form = ReportForm(data)
    # formset = CopyFormSet(data, instance=request.session.get('report_in_creation', Report()))

    if report_form.is_valid():
        report = report_form.save()
        request.session['report_in_creation'] = formset.instance = report
        if formset.is_valid():
            formset.save()
            del request.session['report_in_creation']

    return render(request, 'reports/add.html', locals())


def listing(request, page):
    reports_list = Report.objects.all()
    paginator = Paginator(reports_list, 30)

    reports = paginator.page(page)

    return render(request, 'reports/listing.html', {"reports": reports})
