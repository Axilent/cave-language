# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-14 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cavelanguage', '0002_symbol_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagram',
            name='discussion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
