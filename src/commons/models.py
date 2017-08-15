# -*- coding: utf-8 -*-
#from src.api import models

from django.db import models

from src.commons.types import RequestStatus
from src.users.views import User
from django.utils.translation import ugettext_lazy as _

class Category(models.Model):
    name = models.CharField(('Nombre de la categoria'), max_length=255)
    user = models.ManyToManyField(User, verbose_name=_('User'), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'

class Need(models.Model):
    name = models.CharField(('Nombre de la necesidad'), max_length=255)
    category = models.ForeignKey(Category,verbose_name=_('Category'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Necesidad'


class Schedule(models.Model):
    user = models.ForeignKey(User, verbose_name=_('User'))
    date = models.DateField(verbose_name=_('Dia'))
    time = models.TimeField(_('Hora de atencion'))

    class Meta:
        verbose_name = 'Horario'

class StudentRequest(models.Model):
    student = models.ForeignKey(User, verbose_name=_('User'))
    description = models.TextField(_('Descripción'), blank=True, null=True)
    need = models.ForeignKey(Need, verbose_name=_('Necesidad'))
    schedule = models.ForeignKey(Schedule, verbose_name=_('Horario'))
    status = models.CharField(_('Estado de la peticion'),max_length=255,
    choices=RequestStatus.TYPES,
    default=RequestStatus.ASSIGNED)

    class Meta:
        verbose_name = 'Peticion'




