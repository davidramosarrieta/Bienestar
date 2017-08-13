# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import random

from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User, UserApp


def confirm_account(request, id, template_name = 'email/confirmed_account.html'):
    user = UserApp.objects.filter(confirm_account_id=id)
    message = "URL de confirmacción incorrecta. Por favor verifica."

    if len(user) > 0:
        message = "Genial, cuenta confirmada satisfactoriamente. Puedes ingresar desde tu teléfono."
        user[0].status = UserApp.ENABLE

        token = random.randint(10000,999999999)
        user[0].confirm_account_id = "{0}.434-.{1}32432.-{2}".format(token,
                                                                     user[0].email,
                                                                     user[0].confirm_account_id
                                                                     )
        user[0].save()

    data = {
        "message": message
    }

    return render(request, template_name, data)

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('summary_trips')


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'
