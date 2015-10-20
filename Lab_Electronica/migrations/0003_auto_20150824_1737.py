# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Lab_Electronica', '0002_auto_20150821_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailhistory',
            name='date_out',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
    ]
