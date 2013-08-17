from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Report
from .forms import ReportForm



def add(request):
    form = ReportForm(data=request.POST if request.POST else None)
    if form.is_valid():
        form.save()
    return render(request, 'report.html', locals())