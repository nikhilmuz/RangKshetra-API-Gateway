# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-04 03:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('arts', '0002_auto_20180903_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='uploader',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
