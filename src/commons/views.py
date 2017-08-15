# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from src.commons.requests.forms import RequestForm


@login_required
def summary_trips(request, template_name='dashboard/officers/summary.html'):
    if request.POST:
        form = RequestForm(request=request,data=request.POST or None, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('schedules_officers'))
    else:
        form = RequestForm(request=request)

    data={}
    data['form'] = form

    if request.user.rol == 'Estudiante':
        template_name = 'dashboard/students/request.html'

    return render(request, template_name, data)
