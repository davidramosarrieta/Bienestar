from __future__ import absolute_import, unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from src.commons.models import Schedule, StudentRequest
from src.users.models import User


@login_required
def officer_schedule(request, template_name='dashboard/officers/request.html'):


    student_requests = StudentRequest.objects.filter(schedule__user=request.user)

    context = {
        'student_requests': student_requests
    }
    #return render(template

    return render(request, template_name, context)
