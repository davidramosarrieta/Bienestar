# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from src.commons.models import Schedule
from src.commons.schedules.forms import ScheduleForm


@login_required
def schedules_officers(request, template_name='dashboard/officers/schedules.html'):
    data = {}
    data['time'] = datetime.now()
    data['schedules']= Schedule.objects.filter(user=request.user, date__gte=data['time']).order_by('date','time')

    if request.POST:
        form = ScheduleForm(request=request, data=request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('schedules_officers'))
    else:
        form = ScheduleForm(request=request, initial={
            "date":None,
            "start_time":None,
            "end_time":None,
        })

    data['form'] = form

    return render(request, template_name, data)
