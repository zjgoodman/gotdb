from django.db import models

class Family(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return "House " + self.name

class Person(models.Model):
    first_name  = models.CharField(max_length=50)
    family_name = models.CharField(max_length=50)
    castle_name = models.CharField(max_length=50)

    def __str__(self):
    	return self.first_name + " " + self.family_name

class Castle(models.Model):
    ruling_family = models.ForeignKey(Family)
    name = models.CharField(max_length=100)
