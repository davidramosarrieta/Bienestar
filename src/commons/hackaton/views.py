# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

@login_required
def hackaton(request, template_name='dashboard/hackaton/summary.html'):
    data = {
    }
    data['action'] = "update"
    return render(request, template_name, data)


