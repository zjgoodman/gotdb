from django.db import models

class Person(models.Model) :
    # house = models.ForeignKey(House)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    house_name = models.ForeignKey('House', null=True)
    titles = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    bio = models.TextField() 
    def __str__(self):
        return self.first_name + " " + self.last_name
    #actor_name = models.CharField(max_length=200) 

class Region(models.Model) :
    name = models.CharField(max_length=200)
    # ruling_house = models.ForeignKey('House', null=True)
    # capital = models.ForeignKey('Castle', null=True)
    ruling_lord = models.ForeignKey(Person, null=True)
    description = models.TextField()
    def __str__(self):
        return self.name

class Castle(models.Model) :
    name = models.CharField(max_length=200)
    region = models.ForeignKey(Region, null=True)
    description = models.TextField(null=True)
    ruling_lord = models.ForeignKey(Person, null=True)
    # ruling_house = models.ForeignKey('House', null=True)
    def __str__(self):
        return self.name

class House(models.Model) :
    name = models.CharField(max_length=200)
    region = models.ForeignKey(Region, null=True)
    castle = models.ForeignKey(Castle, null=True)
    description = models.TextField(null=True)
    def __str__(self):
        return self.name
    
# class House(models.Model) :
