# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from src.api.views.location_views import ApiUserLocationView
from src.api.views.message_views import ApiMessagesView
from src.api.views.passenger_request_views import ApiPassengerRequestView
from src.api.views.schedule_views import ApiScheduleView
from src.api.views.trip_views import ApiTripView
from src.api.views.user_views import ApiUserDetailView


urlpatterns = [
    url(
        regex=r'^user/cities$',
        view=ApiUserDetailView.user_cities,
        name='user_cities'
    ),
]
