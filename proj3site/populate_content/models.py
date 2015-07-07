from django.db import models

class Person(models.Model) :
    """
    Person model corresponds to a character in the show.
    A Person has the following attributes that appear on its page:
    - First Name
    - Last Name
    - Actor Name
    - Title
    - House Name (ForeignKey House)
    - Status
    - Bio
    """
    # name info
    person_id = models.CharField(max_length=200, null=True)
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
        ordering = ('last_name',)

class Region(models.Model) :
    """
    Region models correspond to geographical areas.
    A Region has the following attributes that appear on its page:
    - Name
    - Capitol (ForeignKey Castle)
    - Ruling Family (ForeignKey House)
    - Description 
    - History 
    """
    # name
    region_id = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    
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

class Castle(models.Model):
    """
    Castle models correspond to castles.
    A Castle has the following attributes that appear on its page:
    - Name
    - Location (ForeignKey Region)
    - Ruling Family (ForeignKey House)
    - Description
    - History
    """
    # name and region
    castle_id = models.CharField(max_length=200, null=True)
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
    house_id = models.CharField(max_length=200, null=True)
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

class Author(models.Model) :
    # name
    author_id = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)

    # bio
    bio = models.TextField(null=True)

    # major responsibilities
    responsibilities = models.TextField(null=True)

    # statistics
    num_commits = models.IntegerField(null=True)
    num_issues  = models.IntegerField(null=True)
    num_unit_tests = models.IntegerField(null=True)

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ('last_name',)
    
        