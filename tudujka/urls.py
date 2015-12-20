"""tudujka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from tudulist.views import *
from treasurer.views import *
from menu.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^todo/info/[0-9]{1,5}$','tudulist.views.todo_info',name="todo_info"),
    url(r'^todo/add', 'tudulist.views.todo_add',name='tudu_add'),
    url(r'^todo/change/[0-9]{1,5}$', 'tudulist.views.todo_change',name='tudu_change'),
    url(r'^todo/delete/[0-9]{1,5}$','tudulist.views.todo_delete',name="tudu_delete"),
    url(r'^todo', 'tudulist.views.todo',name='tudu'),
    url(r'^treasurer/add', AddCostView.as_view(),name='treasurer_add'),
    url(r'^treasurer/change/(?P<pk>[0-9]+)', ChangeCostView.as_view(),name='treasurer_change'),
    url(r'^treasurer/delete/(?P<pk>[0-9]+)', DeleteCostView.as_view(),name='treasurer_delete'),
    url(r'^treasurer', CostsView.as_view(),name='treasurer'),
    url(r'^options/(?P<pk>[0-9]+)', Options.as_view(),name='options'),
    url(r'^/', 'menu.views.gimme_menu',name='menu'),
    url(r'^', 'menu.views.gimme_menu',name='menu'),
    # url(r'^login', 'tudulist.views.login',name='login'),

]
'''
    url(r'^todo/add', 'tudulist.views.todo_add',name='tudu_add'),
'''