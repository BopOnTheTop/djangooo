# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.conf.urls import include, url
from django.contrib import admin
import re,string
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.defaultfilters import date as _date
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from django.utils import translation
from .models import task
from datetime import datetime

def todo(request):
    '''
    Generating the todo list and POST responses of the forms
    '''
    if request.method == "POST":
        print(request.POST['action'])
        action = str=request.POST['action']
        action = action.split(sep=' ')
        print(action[0])
        if action[0] == 'delete':
            kill = task(id=action[1])
            kill.delete()
            return
        elif action[0] == 'change':
            return
        elif action[0] == 'info':
            return HttpResponseRedirect('todo/info/'+action[1])
        elif action[0] == 'export':
            return


    todo_list = task.objects.all().order_by('id')
    translation.activate("uk")
    # print(_date(datetime.now(),"d b, D"))
    print(request.path)
    return render(request, 'todo.html', {'todo': todo_list})


def todo_info(request):
    path = request.path
    path = path.split(sep='/')
    print(path)
    for i in task.objects.all():
        print(i.quest, i.id)
    item = task.objects.all().filter(id=path[3])
    translation.activate("uk")
    print(item[0].quest)
    return render(request, 'info.html', {'quest' : item[0]} )

def todo_add(request):
    if request.method == "POST":
# was form add button clicked?
        if request.POST.get('add_button') is not None:
            #print('Not wasted')
            #task.objects.all().delete()
            item = [u'\\', u'/', u',', u'.', u'-']
            dick = {}
            for thing in item:
                    dick[ord(thing)]=' '
            print(dick)
            given_uni=request.POST['given'].translate(dick)
            print(given_uni)
            deadline_uni=request.POST['deadline'].translate(dick)
            new_task =  task(quest=request.POST['quest'],
                             whois=request.POST['whois'],
                             given=datetime.strptime(given_uni,'%d %m %Y'),
                             deadline=datetime.strptime(deadline_uni,'%d %m %Y'),
                             done=bool(request.POST['done']),
                             priority=int(request.POST['priority']),
                             progress=request.POST['progress'],
                             notes=request.POST['notes'],
                             )
            new_task.save()
            return HttpResponseRedirect('./')
    return render(request, 'add.html', {})

def todo_change(request):

    return HttpResponse('<h1>Student Change Form</h1>')

def todo_delete(request):
    task.objects()

    return HttpResponseRedirect('todo')