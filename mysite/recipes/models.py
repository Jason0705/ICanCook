from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Recipe(models.Model):
	rid = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	userid = models.IntegerField()
	prep_time = models.IntegerField()

	def __str__(self):
		return ("%i, %s, %s, %i, %i" % (self.rid, self.title, self.description, self.userid, self.prep_time))

class Step(models.Model):
	rid = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	description = models.CharField(max_length=1000)
	order = models.CharField(max_length=25)

	def __str__(self):
		return self.rid

class QuantityType(models.Model):
	qid = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=25)

	def __str__(self):
		return self.name

class Ingredient(models.Model):
	rid = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	name = models.CharField(max_length=25)
	quantity = models.IntegerField()
	quantity_type = models.ForeignKey(QuantityType)

	def __str__(self):
		return self.name
