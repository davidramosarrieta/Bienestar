# -*- coding: utf-8 -*-
#from src.api import models

from django.db import models

from src.commons.types import RequestStatus
from src.users.views import User
from django.utils.translation import ugettext_lazy as _

#class OrganizationLevelInstance(models.Model):
#    organization_level = models.ForeignKey(verbose_name=_('Ni'))
#    name = models.CharField(_('Nombre'), max_length=255)
#    external_website = models.CharField(_('Sitio web externo'), max_length=255, blank=True, null=True)
#    abbreviation = models.CharField(_('Abreviación'), max_length=255, blank=True, null=True)
#    country = models.ForeignKey(Country, verbose_name=_('País'), blank=True, null=True)
#    state = models.ForeignKey(State, verbose_name=_('Departamento'), blank=True, null=True)
#    city = models.ForeignKey(City, verbose_name=_('Ciudad administrativa'), blank=True, null=True)
#    address = models.CharField(_('Dirección'), max_length=512, blank=True, null=True)
#    lat = models.CharField(_('Latitud'), max_length=512, blank=True, null=True)
#    lng = models.CharField(_('Longitud'), max_length=512, blank=True, null=True)
#    picture = models.ImageField(_('Imagen'), upload_to=get_instance_path, max_length=512, blank=True, null=True)
#    phone = models.CharField(_('Teléfono'), max_length=512, default="")
#    parent = models.ForeignKey('self', blank=True, null=True,verbose_name=_('Sede de la cual depende'))
#    city_fractions = models.ManyToManyField(CityFraction, verbose_name=_('Ciudades a cargo'), related_name='cities')
#    place_id = models.CharField(_('Id de sitio en google maps'), max_length=255, blank=True, null=True)




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


class Shedule(models.Model):
    user = models.ForeignKey(User, verbose_name=_('User'))
    date = models.DateField(verbose_name=_('Dia'))
    time = models.TimeField(_('Hora de atencion'))

    class Meta:
        verbose_name = 'Horario'

class StudentRequest(models.Model):
    student = models.ForeignKey(User, verbose_name=_('User'))
    description = models.TextField(_('Descripción'), blank=True, null=True)
    need = models.ForeignKey(Need, verbose_name=_('Necesidad'))
    shedule = models.ForeignKey(Shedule, verbose_name=_('Horario'))
    status = models.CharField(_('Estado de la peticion'),max_length=255,
    choices=RequestStatus.TYPES,
    default=RequestStatus.ASSIGNED)

    class Meta:
        verbose_name = 'Peticion'




