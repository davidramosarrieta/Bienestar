# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms
from django.contrib import admin

from src.commons.models import Category, Need


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','user')

admin.site.register(Category, CategoryAdmin)



class NeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')

admin.site.register(Need, NeedAdmin)






