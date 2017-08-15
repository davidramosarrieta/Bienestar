# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin

from src.commons.models import Category, Need, Schedule, StudentRequest


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)

class NeedAdmin(admin.ModelAdmin):
    list_display = ('name','category')

admin.site.register(Need, NeedAdmin)

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('user','date','time',)

admin.site.register(Schedule, ScheduleAdmin)

class StudentRequestAdmin(admin.ModelAdmin):
    list_display = ('student','need','schedule','status',    )

admin.site.register(StudentRequest, StudentRequestAdmin)
