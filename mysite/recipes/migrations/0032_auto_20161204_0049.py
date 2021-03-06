# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0031_merge_20161201_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='dessert',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='holiday',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quantitytype',
            name='short_name',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='quantitytype',
            name='use_fraction',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recipe',
            name='calorie',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
