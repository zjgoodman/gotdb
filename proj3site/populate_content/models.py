from django.db import models

class Person(models.Model) :
    # house = models.ForeignKey(House)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    titles = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    bio = models.TextField() 
    def __str__(self):
        return self.first_name + " " + self.last_name
    #actor_name = models.CharField(max_length=200) 

class Region(models.Model) :
    name = models.CharField(max_length=200)
    # capital = models.ForeignKey(Castle)
    description = models.TextField()
    def __str__(self):
        return self.name

class Castle(models.Model) :
    name = models.CharField(max_length=200)
    region = models.ForeignKey(Region)
    def __str__(self):
        return self.name
    
# class House(models.Model) :
