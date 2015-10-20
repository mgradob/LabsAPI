# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Lab_Electronica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailhistory',
            name='date_out',
            field=models.DateTimeField(default=datetime.datetime.now, null=True, blank=True),
            preserve_default=True,
        ),
    ]
