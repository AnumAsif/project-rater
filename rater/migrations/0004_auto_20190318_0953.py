# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-18 06:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rater', '0003_language'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ('title',)},
        ),
        migrations.AddField(
            model_name='language',
            name='projects',
            field=models.ManyToManyField(to='rater.Project'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contact_no',
            field=models.IntegerField(null=True),
        ),
    ]
