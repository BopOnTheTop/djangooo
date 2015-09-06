from django.shortcuts import render
from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse
# Create your views here.


def todo(request):
    return render(request, 'todo.html', {})


def todo_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

