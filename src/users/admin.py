# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User, UserApp, Group, City, Location, Plate, UserDevice, UserCurrentLocation, UserHistoricalLocation, \
    UserRating, LocationFilter


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address','userApp')

admin.site.register(Location, LocationAdmin)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain')

admin.site.register(Group, GroupAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = ('name','group')

admin.site.register(City, CityAdmin)

class UserAppAdmin(admin.ModelAdmin):
    list_display = ('name','group','email','status')

admin.site.register(UserApp, UserAppAdmin)

class PlateAdmin(admin.ModelAdmin):
    list_display = ('plate',)

admin.site.register(Plate, PlateAdmin)


class UserCurrentLocationAdmin(admin.ModelAdmin):
    list_display = ('userApp','latitude','longitude')

admin.site.register(UserCurrentLocation, UserCurrentLocationAdmin)

class UserHistoricalLocationAdmin(admin.ModelAdmin):
    list_display = ('userApp','latitude','longitude')

admin.site.register(UserHistoricalLocation, UserHistoricalLocationAdmin)

class UserDeviceAdmin(admin.ModelAdmin):
    list_display = ('userApp','platform')

admin.site.register(UserDevice, UserDeviceAdmin)

class UserRatingAdmin(admin.ModelAdmin):
    list_display = ('userApp','rol', 'score')

admin.site.register(UserRating, UserRatingAdmin)

class LocationFilterAdmin(admin.ModelAdmin):
    list_display = ('userApp','active', 'address_begin','address_end')

admin.site.register(LocationFilter, LocationFilterAdmin)

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):

    error_message = UserCreationForm.error_messages.update({
        'duplicate_username': 'This username has already been taken.'
    })

    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


@admin.register(User)
class MyUserAdmin(AuthUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = (
            ('User Profile', {'fields': ('name',)}),
    ) + AuthUserAdmin.fieldsets
    list_display = ('username', 'name', 'is_superuser')
    search_fields = ['name']
