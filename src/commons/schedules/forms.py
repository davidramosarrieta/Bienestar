# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from django import forms
from django.utils.translation import ugettext_lazy as _

from src.commons.models import Schedule


class ScheduleForm(forms.Form):
    date = forms.DateField(label=_('Dia disponible'), required=True,
                                 widget=forms.TextInput(attrs={
                                     'class': 'datepicker gui-input',
                                     'placeholder': 'Día disponible.','required':'',
                                 }))
    start_time = forms.TimeField(label=_('Hora disponible'), required=True,
                                 widget=forms.TimeInput(attrs={
                                     'class': 'timepicker form-control gui-input',
                                     'placeholder': 'Desde.','required':''
                                 }))

    end_time = forms.TimeField(label=_('Hora disponible'), required=True,
                                 widget=forms.TimeInput(attrs={
                                     'class': 'timepicker form-control gui-input',
                                     'placeholder': 'Hasta.','required':''
                                 }))

    def __init__(self, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)

    def save(self, schedule=None, data=None):
        start = self.cleaned_data['start_date']
        end = self.cleaned_data['end_date']
        date = self.cleaned_data['date']
        if not schedule:
            while start <= end:
                schedule = Schedule(
                    user=data.user,
                    date=date,
                    time=start,
                )
                schedule.save()
                start = start + timedelta(hours=1)
        else:
            schedule.date=self.cleaned_data['date']
            schedule.time = self.cleaned_data['time']
            schedule.save()
        return schedule
