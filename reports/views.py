from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Reports
from .forms import ReportsForm



def add(request):
    form = ReportsForm(data=request.POST if request.POST else None)
    if form.is_valid():
        form.save()
    return render(request, 'report.html', locals())