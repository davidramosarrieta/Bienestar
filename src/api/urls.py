# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import url, include
from src.api.views.user_views import ApiUserDetailView


urlpatterns = [
    url(
        regex=r'^user/cities$',
        view=ApiUserDetailView.user_cities,
        name='user_cities'
    ),
]
