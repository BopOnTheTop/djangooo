# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
import re,string
from django.shortcuts import render
from django import forms
from treasurer.forms import CostForm
from django.views.generic.edit import FormView,UpdateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView,DeleteView
from django.contrib.auth.models import User
from django.http import HttpResponse ,HttpResponseRedirect
from django.template.defaultfilters import date as _date
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.http import Http404
# Create your views here.
from django.utils import translation
from datetime import datetime
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.core.urlresolvers import reverse_lazy
from .models import *

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class AddCostView(CreateView):
    """
    CBS for an add-cost-page.
    """
    fields = [ 'credit','debit','percent','date','from_who','who_to','what_for','notes',]
    model = cost
    template_name = "cost_t.html"
    success_url = '/treasurer/'

class ChangeCostView(UpdateView):
    """
    CBS for change-cost-pages
    """
    model = cost
    template_name = "update.html"
    fields = [ 'credit','debit','percent','date','from_who','who_to','what_for','notes',]
    success_url = reverse_lazy('treasurer')

class DeleteCostView(DeleteView):
    model = cost
    context_object_name = "cost"
    template_name = "del_t.html"
    success_url = '/treasurer/'

class CostsView(ListView):
    model = cost
    context_object_name = "cost"
    template_name = "list.html"
    def get_context_data(self, **kwargs):
        context = super(CostsView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        rez = 0
        for item in cost.objects.all():
            rez += item.debit
            rez -= item.credit
        context['rez'] = rez
        return context