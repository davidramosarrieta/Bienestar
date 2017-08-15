# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-08-15 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0002_auto_20170815_1204'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shedule',
            new_name='Schedule',
        ),
        migrations.RenameField(
            model_name='studentrequest',
            old_name='shedule',
            new_name='schedule',
        ),
        migrations.AlterField(
            model_name='need',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nombre de la necesidad'),
        ),
    ]