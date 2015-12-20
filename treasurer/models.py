# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.

class cost(models.Model):
    """Task Model"""
    id = models.IntegerField(primary_key=True, unique=True, db_index=True)
    credit = models.IntegerField( blank=True, verbose_name=u"Кредит")
    debit = models.IntegerField(blank=True, verbose_name=u"Дебет", null=True)
    what_for = models.CharField(max_length=256,blank=True, verbose_name=u"На що", null=True)
    notes = models.TextField(blank=True, verbose_name=u"Додаткові нотатки")
    percent = models.IntegerField(blank=True, verbose_name=u"Проценти")
    date = models.DateField(blank=True, verbose_name=u"Коли", null=True)
    from_who = models.CharField(max_length=256, blank=True, verbose_name=u"Від кого")
    who_to = models.CharField(max_length=256, blank=True, verbose_name=u"Кому")

