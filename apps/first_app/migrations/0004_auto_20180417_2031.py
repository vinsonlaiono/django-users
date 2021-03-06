# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-18 03:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20180417_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='blogs',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='blog',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='name',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='desc',
        ),
        migrations.AddField(
            model_name='blog',
            name='first_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='last_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
