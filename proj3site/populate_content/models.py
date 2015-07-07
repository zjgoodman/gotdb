from django.db import models

class Person(models.Model) :
    # name info
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    house_name = models.ForeignKey('House', null=True)

    # titles
    titles = models.CharField(max_length=200, null=True)

    # alive or dead
    status = models.CharField(max_length=200, null=True)

    # short biographical information
    bio = models.TextField(null=True) 

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ('first_name',)

class Region(models.Model) :
    # name
    name = models.CharField(max_length=200)
    
    # capital
    capital_name = models.ForeignKey('Castle', null=True)

    # ruling family and lord
    ruling_house = models.ForeignKey('House', null=True)
    ruling_lord = models.ForeignKey(Person, null=True)

    # brief description
    description = models.TextField(null=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Castle(models.Model) :
    # name and region
    name = models.CharField(max_length=200, null=True)
    region_name = models.ForeignKey(Region, null=True)

    # ruling house and lord
    ruling_house = models.ForeignKey('House', null=True)
    ruling_lord = models.ForeignKey(Person, null=True)

    # brief description
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class House(models.Model) :
    # name
    name = models.CharField(max_length=200, null=True)

    # famous expressions
    words = models.CharField(max_length=300, null=True)

    # region of the world
    region_name = models.ForeignKey(Region, null=True)

    # the name of their castle
    castle_name = models.ForeignKey(Castle, null=True)

    # brief description
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
