from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Recipe(models.Model):
    rid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    userid = models.IntegerField()
    prep_time = models.IntegerField()

    def __str__(self):
        return "RID: %i, TITLE: %s" % (self.rid, self.title)


class Step(models.Model):
    rid = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    order = models.IntegerField()

    def __str__(self):
        return "DESCRIPTION: %s, ORDER: %s" % (self.description, self.order)


class QuantityType(models.Model):
    qid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return "QID: %i, NAME: %s" % (self.qid, self.name)


class Ingredient(models.Model):
    rid = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    quantity = models.IntegerField()
    quantity_type = models.ForeignKey(QuantityType)

    def __str__(self):
        return "NAME: %s, QUANTITY: %s" % (self.name, self.quantity)
