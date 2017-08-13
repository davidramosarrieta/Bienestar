# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

@python_2_unicode_compatible
class User(AbstractUser):

    name = models.CharField(_('Nombre completo'), max_length=512)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    class Meta:
        verbose_name = 'Usuario'

@python_2_unicode_compatible
class City(models.Model):

    name = models.CharField(_('Nombre'), max_length=255)
    latitude = models.CharField(_('Latitud'), max_length=255)
    longitude = models.CharField(_('Longitud'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ciudades'


#@receiver(models.signals.pre_save, sender=UserApp)
def update_file_from_s3(sender, instance, using, **kwargs):
    try:
        if sender.objects.filter(id = instance.pk).exists():
            old = sender.objects.get(pk=instance.pk)
            if old.picture != instance.picture:
                old.picture.delete(save=False)
    except Exception as e:
        print (e)


#@receiver(models.signals.post_delete, sender=UserApp)
def remove_file_from_s3(sender, instance, using, **kwargs):
    instance.picture.delete(save=False)

