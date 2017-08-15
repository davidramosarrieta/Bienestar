from __future__ import absolute_import, unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from src.commons.models import Schedule
from src.commons.nedds.forms import NeedForm

@login_required
def request_students(request, template_name='dashboard/students/request.html'):
    data = {}

    if request.POST:
        form = NeedForm(data=request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('dashboard/students/request.html')
    else:
        form = NeedForm()

    data['form'] = form
    return render(request, template_name, data)
