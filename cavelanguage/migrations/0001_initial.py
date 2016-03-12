# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-12 15:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djax.content


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('body', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Diagram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.URLField(max_length=500)),
                ('download', models.URLField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Symbol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField()),
                ('url', models.URLField(max_length=500, null=True)),
                ('categories', models.ManyToManyField(related_name='symbols', to='cavelanguage.Category')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='symbols', to='cavelanguage.Collection')),
            ],
            bases=(models.Model, djax.content.ACEContent),
        ),
        migrations.AddField(
            model_name='diagram',
            name='symbols',
            field=models.ManyToManyField(related_name='diagrams', to='cavelanguage.Symbol'),
        ),
        migrations.AddField(
            model_name='category',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='cavelanguage.Collection'),
        ),
        migrations.AddField(
            model_name='article',
            name='diagrams',
            field=models.ManyToManyField(related_name='articles', to='cavelanguage.Diagram'),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([('collection', 'name')]),
        ),
    ]
