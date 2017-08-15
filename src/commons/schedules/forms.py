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

    def __init__(self, request, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)
        self.user = request.user

    def save(self):
        start = self.cleaned_data['start_time']
        end = self.cleaned_data['end_time']
        date = self.cleaned_data['date']
        while start <= end:
            schedule = Schedule(
                user=self.user,
                date=date,
                time=start,
            )
            schedule.save()
            start = (datetime.combine(date.today(), start) + timedelta(hours=1)).time()

