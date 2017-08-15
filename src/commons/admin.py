# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms
from django.contrib import admin

from src.commons.models import Category, Need, Shedule, StudentRequest


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)

class NeedAdmin(admin.ModelAdmin):
    list_display = ('name','category')

admin.site.register(Need, NeedAdmin)

class SheduleAdmin(admin.ModelAdmin):
    list_display = ('user','date','time',)

admin.site.register(Shedule, SheduleAdmin)

class StudentRequestAdmin(admin.ModelAdmin):
    list_display = ('student','need','shedule','status',    )

admin.site.register(StudentRequest, StudentRequestAdmin)




