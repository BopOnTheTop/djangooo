__author__ = 'masterbob'

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class options(models.Model):
    id=models.IntegerField(primary_key=True, auto_created=True, unique=True)
    signals = models.BooleanField()