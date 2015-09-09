# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class task(models.Model):
    """Task Model"""
    id = models.IntegerField(primary_key=True,unique=True,db_index=True)
    quest = models.CharField(max_length=256,blank=False,verbose_name=u"Квест")
    given = models.DateField(blank=False,verbose_name=u"Видано",null=True)
    deadline= models.DateField(blank=False,verbose_name=u"Дедлайн",null=True)
    notes = models.TextField(blank=True,verbose_name=u"Додаткові нотатки")
    done = models.BooleanField(blank=True,verbose_name=u"Здано")
    progress = models.CharField(blank=True,max_length=256,verbose_name=u"Зроблено",null=True)
    whois = models.CharField(max_length=256,blank=True,verbose_name=u"Квестодавець")
    priority = models.IntegerField(verbose_name="Пріоритет",null=True)
