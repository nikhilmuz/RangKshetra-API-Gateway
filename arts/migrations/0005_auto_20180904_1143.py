# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-04 11:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0004_auto_20180904_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='uploader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arts', to=settings.AUTH_USER_MODEL),
        ),
    ]