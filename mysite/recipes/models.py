from __future__ import unicode_literals

from django.db import models


class Recipe(models.Model):
    rid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    userid = models.IntegerField()
    prep_time = models.FloatField()
    recipe_pic = models.FileField(null=True, blank=True) #upload_to='recipes/static/recipes/images/', 
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

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    rid = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    quantity_type = models.ForeignKey(QuantityType)

    def __str__(self):
        return "NAME: %s, QUANTITY: %s" % (self.name, self.quantity)
