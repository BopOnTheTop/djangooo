# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import render
from django import forms
from tudulist.forms import QuestForm
from django.views.generic.edit import FormView,UpdateView
from django.contrib.auth.models import User
from django.http import HttpResponse ,HttpResponseRedirect
from django.template.defaultfilters import date as _date
from django.core.urlresolvers import reverse
from datetime import datetime
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.views.generic import View
from django.contrib.auth import logout
from django.core.urlresolvers import reverse_lazy
from .models import options
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def gimme_menu(request):
    return render(request, "menu.html", {'date' : datetime.now().date()})

class Options(UpdateView):
    """
    CBS for changing options page
    """
    pk = 1
    model = options
    template_name = "update.html"
    fields = [ 'signals',]
    success_url = "/"


class LogoutAskView(DetailView):
    
    template_name = "logout.html"
    

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
