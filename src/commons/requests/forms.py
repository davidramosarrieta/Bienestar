# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from src.commons.models import Need, StudentRequest, Schedule


class RequestForm(forms.Form):
    description= forms.CharField(label=_('Descripcion'),
                           widget=forms.Textarea(attrs={
                               'required':'',
                                'class':'form-control gui-input',
                               'placeholder':'Has un comentario de tu solicitud.'
                           }), required=False)
    need = forms.ModelChoiceField(label=_('Tipo de necesidad'), queryset=Need.objects.all(),
                            widget=forms.Select(attrs={
                                'required': '',
                                'class':'form-control gui-input',
                                'placeholder':'solicitud.'
                            }))
    schedule = forms.ModelChoiceField(label=_('Tipo de necesidad'), queryset=Schedule.objects.all(),
                            widget=forms.Select(attrs={
                                'required': '',
                                'class':'form-control gui-input'
                            }))


    def __init__(self, request, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.student = request.user

    def save(self, instance=None):
        if not instance:
            instance = StudentRequest(
            description = self.cleaned_data['description'],
            need = self.cleaned_data['need'],
            schedule=self.cleaned_data['schedule'],
            student = self.student,
            )
            instance.save()

        return instance


