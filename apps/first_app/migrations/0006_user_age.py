# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-18 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_auto_20180417_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0, verbose_name=0),
            preserve_default=False,
        ),
    ]
