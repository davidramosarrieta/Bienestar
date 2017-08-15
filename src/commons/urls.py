# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import url

from src.commons.schedules.views import schedules_officers
from . import views
from src.commons.hackaton.views import  hackaton

urlpatterns = [
    url(
        regex=r'^$',
        view=views.summary_trips,
        name='summary_trips'
    ),
    url(
        regex=r'^hackaton$',
        view=hackaton,
        name='summary_trips'
    ),
    url(
        regex=r'^funcionario/horario$',
        view=schedules_officers,
        name='schedules_officers'
    ),
]
