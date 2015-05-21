# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True)),
                ('id_administrator', models.CharField(max_length=10, unique=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('last_name_1', models.CharField(max_length=50)),
                ('last_name_2', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Labs',
            fields=[
                ('name', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('link', models.URLField(max_length=500)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True)),
                ('id_student', models.CharField(max_length=10, unique=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('last_name_1', models.CharField(max_length=50)),
                ('last_name_2', models.CharField(max_length=50)),
                ('id_credential', models.IntegerField(null=True)),
                ('career', models.CharField(max_length=5)),
                ('mail', models.EmailField(max_length=254)),
                ('labs', models.ManyToManyField(to='LabsIndex.Labs')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='administrator',
            name='labs',
            field=models.ManyToManyField(to='LabsIndex.Labs'),
        ),
    ]
