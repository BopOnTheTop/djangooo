# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tudulist', '0003_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='progress',
            field=models.CharField(blank=True, max_length=256, verbose_name='Зроблено', null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='given',
            field=models.DateField(verbose_name='Видано', null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.IntegerField(primary_key=True, unique=True, serialize=False, db_index=True),
        ),
    ]
