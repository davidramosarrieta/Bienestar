# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from src.commons.models import Schedule


@login_required
def schedules_officers(request, template_name='dashboard/officers/schedules.html'):
    data = {}
    data['time'] = datetime.now()
    data['schedules']= Schedule.objects.filter(user=request.user)

    return render(request, template_name, data)
