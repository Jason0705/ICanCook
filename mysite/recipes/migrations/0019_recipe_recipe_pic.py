# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0018_remove_recipe_recipe_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_pic',
            field=models.ImageField(default='static/recipes/images/blank.jpg', upload_to='static/recipes/images/'),
        ),
    ]
