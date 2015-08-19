# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LabsIndex', '0002_auto_20150521_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='last_login',
            field=models.DateTimeField(verbose_name='last login',blank=True),
        ),
    ]
