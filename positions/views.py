# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .forms import PositionForm


@permission_required('positions.add_position')
def add(request):
    data = request.POST if request.POST else None
    position_form = PositionForm(data)
    if position_form.is_valid():
        position_form.save()
    return render(request, 'positions/add_form.html', {'position_form': position_form})
