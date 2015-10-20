# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id_category', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id_component', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('note', models.CharField(max_length=250, null=True)),
                ('total', models.IntegerField()),
                ('available', models.IntegerField()),
                ('id_category_fk', models.ForeignKey(related_name='category', to='Lab_Electronica.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DetailCart',
            fields=[
                ('quantity', models.IntegerField()),
                ('checkout', models.BooleanField(default=False)),
                ('ready', models.BooleanField(default=False)),
                ('date_checkout', models.DateTimeField(null=True, blank=True)),
                ('id_cart', models.AutoField(serialize=False, primary_key=True)),
                ('id_component_fk', models.ForeignKey(related_name='component_cart', to='Lab_Electronica.Component')),
                ('id_student_fk', models.ForeignKey(related_name='student_cart', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DetailHistory',
            fields=[
                ('quantity', models.IntegerField()),
                ('date_out', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('date_in', models.DateTimeField(null=True, blank=True)),
                ('id_history', models.AutoField(serialize=False, primary_key=True)),
                ('id_component_fk', models.ForeignKey(related_name='component_history', to='Lab_Electronica.Component')),
                ('id_student_fk', models.ForeignKey(related_name='student_history', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
