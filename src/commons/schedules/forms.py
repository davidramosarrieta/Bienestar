# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from django import forms
from django.utils.translation import ugettext_lazy as _

from src.commons.models import Schedule


class ScheduleForm(forms.Form):
    date = forms.DateField(label=_('Dia disponible'),
                                 widget=forms.TextInput(attrs={
                                     'class': 'datepicker gui-input',
                                     'placeholder': 'Día disponible.'
                                 }))
    start_time = forms.TimeField(label=_('Hora disponible'),
                                 widget=forms.TimeInput(attrs={
                                     'class': 'timepicker form-control gui-input',
                                     'placeholder': 'Desde.'
                                 }))

    end_time = forms.TimeField(label=_('Hora disponible'),
                                 widget=forms.TimeInput(attrs={
                                     'class': 'timepicker form-control gui-input',
                                     'placeholder': 'Hasta.'
                                 }))

    def __init__(self, date, start_time, end_time, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)
        self.date = date
        self.start_time = start_time
        self.end_time = end_time

    def save(self, schedule=None, data=None):
        start = self.start_time
        end = self.end_time
        if not schedule:
            while start <= end:
                schedule = Schedule(
                    user=data.user,
                    date=self.cleaned_data['date'],
                    time=start,
                )
                schedule.save()
                start = start + timedelta(hours=1)
        else:
            schedule.date=self.cleaned_data['date']
            schedule.time = self.cleaned_data['time']
            schedule.save()
        return schedule
