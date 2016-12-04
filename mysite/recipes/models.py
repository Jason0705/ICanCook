from __future__ import unicode_literals

import os
import uuid

from django.db import models
from django.contrib.auth.models import User


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('media', filename)


class Recipe(models.Model):
    rid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    userid = models.IntegerField()
    favourites = models.ManyToManyField(User)
    prep_time = models.FloatField()
    recipe_pic = models.FileField(null=True, blank=True, upload_to=get_file_path)  # upload_to='recipes/static/recipes/images/',
    calorie = models.IntegerField(null=True, blank=True)
    serving = models.IntegerField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "RID: %i, TITLE: %s" % (self.rid, self.title)

    def get_absolute_url(self):
        return "/recipes/%s/" % self.rid

    class Meta:
        ordering = ["-created", "-updated"]


class Step(models.Model):
    rid = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    order = models.IntegerField()

    def __str__(self):
        return "DESCRIPTION: %s, ORDER: %s" % (self.description, self.order)


class QuantityType(models.Model):
    qid = models.IntegerField(primary_key=True)
    name = models.CharField(blank=True, max_length=25)
    short_name = models.CharField(blank=True, max_length=5)
    use_fraction = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    rid = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    quantity_type = models.ForeignKey(QuantityType)

    def __str__(self):
        return "NAME: %s, QUANTITY: %s" % (self.name, self.quantity)

class Category(models.Model):
    rid = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    breakfast = models.BooleanField()
    lunch = models.BooleanField()
    dinner = models.BooleanField()
    dessert = models.BooleanField()
    holiday = models.BooleanField()

    def __str__(self):
        return "BREAKFAST: %s, LUNCH: %s, DINNER: %s, DESSERT: %s, HOLIDAY: %s" % (self.breakfast, self.lunch, self.dinner, self.dessert, self.holiday)
