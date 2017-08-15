# -*- coding: utf-8 -*-
from datetime import datetime

from django import forms
from django.utils.translation import ugettext_lazy as _

from src.commons.models import Shedule


class ScheduleForm(forms.Form):
    date = forms.DateField(label=_('Dia disponible'),
                                 widget=forms.TextInput(attrs={
                                     'class': 'datepicker gui-input',
                                     'placeholder': 'Día disponible.'
                                 }))
    time = forms.TimeField(label=_('Hora disponible'),
                                 widget=forms.TimeInput(attrs={
                                     'class': 'timepicker form-control gui-input',
                                     'placeholder': 'Hora disponible.'
                                 }))

    def __init__(self,  *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)

    def save(self, schedule=None):
        if not schedule:
            schedule = Shedule(
                user=self.cleaned_data['user'],
                date=self.cleaned_data['date'],
                time=self.cleaned_data['time'],
            )
            schedule.save()
        else:
            schedule.name=self.cleaned_data['name']
            schedule.description=self.cleaned_data['description']
            schedule.picture=self.cleaned_data['picture']
            schedule.hide_banner_text=self.cleaned_data['hide_banner_text']
            schedule.external_url=self.cleaned_data['external_url']
            schedule.external_publish_date=datetime.now()
            schedule.order=self.cleaned_data['order']
            schedule.status = self.cleaned_data['status']
            schedule.save()
        return schedule
