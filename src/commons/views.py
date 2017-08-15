# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

@login_required
def summary_trips(request, template_name='dashboard/officers/summary.html'):
    data = {
        'green_trips': [],
        'yellow_trips': [],
        'red_trips': []
    }
    if request.user.rol == 'Estudiante':
        template_name = 'dashboard/students/request.html'

    return render(request, template_name, data)
