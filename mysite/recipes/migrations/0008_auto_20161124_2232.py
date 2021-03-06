# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 22:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_auto_20161119_0509'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='step',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
