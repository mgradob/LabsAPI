# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('LabsIndex', '0003_auto_20150521_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='last_login',
            field=models.DateTimeField(null=True,default=django.utils.timezone.now, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='administrator',
            name='mail',
            field=models.EmailField(max_length=75),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_login',
            field=models.DateTimeField(null=True,default=django.utils.timezone.now, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='student',
            name='mail',
            field=models.EmailField(max_length=75),
        ),
    ]
