# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-08 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0007_auto_20180904_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='art',
            field=models.FilePathField(),
        ),
    ]
