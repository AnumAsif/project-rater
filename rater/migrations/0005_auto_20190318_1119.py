# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-18 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rater', '0004_auto_20190318_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='projects',
        ),
        migrations.AddField(
            model_name='project',
            name='languages',
            field=models.ManyToManyField(to='rater.Language'),
        ),
    ]
