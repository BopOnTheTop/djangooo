# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('quest', models.CharField(verbose_name='Квест', max_length=256)),
                ('given', models.DateField(verbose_name='Видали', null=True)),
                ('deadline', models.DateField(verbose_name='Дедлайн', null=True)),
                ('notes', models.TextField(blank=True, verbose_name='Додаткові нотатки')),
                ('done', models.CharField(blank=True, verbose_name='Квестодавець', max_length=256)),
            ],
        ),
    ]
