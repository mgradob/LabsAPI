# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('LabsIndex', '0004_auto_20150819_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login'),
            preserve_default=True,
        ),
        migrations.AlterModelTable(
            name='student',
            table='Student',
        ),
    ]
