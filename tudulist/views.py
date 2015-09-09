# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def todo(request):
    todo_list = ({
        'id' : 1,
    'quest' : 'Запиляти тудуйку',
    'given' : '1 червня 2015',
    'deadline' : '31 липня 2015',
    'notes' : 'Нема',
    'done' : '',
    'progress' : 'Ніхуа(майже)',
    'whois' : 'Йа',
    'priority' : 5,},
        {
        'id' : 2,
    'quest' : 'Дістати методички лаб',
    'given' : '7 вересня 2015',
    'deadline' : '12 вересня 2015',
    'notes' : 'Нема',
    'done' : '',
    'progress' : 'Чуть-чуть',
    'whois' : 'Йа',
    'priority' : 3,}

    )
    return render(request, 'todo.html', {'todo': todo_list})


def todo_add(request):
    return render(request, 'add.html', {})

def todo_change(request):

    return HttpResponse('<h1>Student Change Form</h1>')

