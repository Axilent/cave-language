# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-20 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cavelanguage', '0006_contributor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='pic',
            field=models.URLField(max_length=500, null=True),
        ),
    ]