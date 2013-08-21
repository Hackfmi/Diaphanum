# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .forms import PositionForm


def can_add_positions(user):
    return user.is_authenticated() and user.has_perm('positions.add_position')


@user_passes_test(can_add_positions)
def add(request):
    data = request.POST if request.POST else None

    position_form = PositionForm(data)
    if position_form.is_valid():
        position_form.save()

    return render(request, 'positions/add_form.html', {'position_form': position_form})