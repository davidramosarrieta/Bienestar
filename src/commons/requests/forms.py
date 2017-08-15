# -*- coding: utf-8 -*-
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from src.commons.models import Need, StudentRequest


class RequestForm(forms.Form):
    description = forms.CharField(widget=CKEditorUploadingWidget(), required=False)
    need = forms.ModelChoiceField(label=_('Tipo de necesidad'), queryset=Need.objects.none(),
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
            student = self.student,

            )
            instance.save()
        else:
            instance.description=self.cleaned_data['description']
            instance.need=self.cleaned_data['need']
            instance.save()

        return instance


