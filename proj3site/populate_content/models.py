from django.db import models

class Person(models.Model) :
    """
    Person model corresponds to a character in the show.
    A Person has the following attributes that appear on its page:
    - First Name
    - Last Name
    - Actor Name
    - Region From (ForeignKey Region)
    - Title
    - House Name (ForeignKey House)
    - Status
    - Bio
    """
    # name info
    person_id      = models.CharField(max_length=200, null=True)
    first_name     = models.CharField(max_length=200, null=True)
    last_name      = models.CharField(max_length=200, null=True)

    # houses associated with
    houses         = models.ManyToManyField('House', blank=True, related_name='person_houses')
    loyal_to       = models.ManyToManyField('House', blank=True, related_name='person_houses_loyal_to')

    # castles that this person controls
    castles_controlled = models.ManyToManyField('Castle', blank=True, related_name='person_castles_owned')

    region_from    = models.ForeignKey('Region', null=True)

    # titles and actor
    titles         = models.TextField(null=True)
    actor          = models.CharField(max_length=200, null=True)

    # alive or dead
    status         = models.CharField(max_length=200, null=True)

    # killer
    #cause_of_death = models.CharField(max_length=200, null=True)
    #killer         = models.ForeignKey('Person', null=True)

    # short biographical information
    bio            = models.TextField(null=True)

    def __str__(self):
        if not self.last_name :
            return self.first_name
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ('last_name', 'first_name')

class Region(models.Model) :
    """
    Region models correspond to geographical areas.
    A Region has the following attributes that appear on its page:
    - Name
    - Capitol (ForeignKey Castle)
    - Ruling Family (ForeignKey House)
    - Ruling Lord (ForeignKey Person)
    - Description 
    - History 
    """
    # name
    region_id  = models.CharField(max_length=200, null=True)
    name       = models.CharField(max_length=200, null=True)
    
    # capital
    capital_name  = models.ForeignKey('Castle', null=True)
    other_castles = models.ManyToManyField('Castle', blank=True, related_name='castles_in_region')

    # ruling family
    ruling_house           = models.ForeignKey('House', null=True)
    # families that used to rule
    previous_ruling_houses = models.ManyToManyField('House', blank=True, related_name='previous_ruling_houses')
    # houses found in this region
    resident_houses        = models.ManyToManyField('House', blank=True, related_name='houses_in_this_region')

    # information
    description   = models.TextField(null=True)
    history       = models.TextField(null=True)

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
    - Ruling Lord (ForeignKey Person)
    - Description
    - History
    """
    # name and region
    castle_id       = models.CharField(max_length=200, null=True)
    name            = models.CharField(max_length=200, null=True)
    region_name     = models.ForeignKey(Region, null=True)

    # ruling house and lord
    #primary_house   = models.ForeignKey('House', null=True)
    # houses that once controlled this castle
    previous_houses = models.ManyToManyField('House', blank=True, related_name='castle_previous_houses')
    
    # lords of the castle
    #primary_lord    = models.ForeignKey(Person, null=True)
    previous_lords  = models.ManyToManyField(Person, blank=True, related_name='castle_previous_lords')

    # brief description
    description     = models.TextField(null=True)
    history         = models.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class House(models.Model) :
    """
    House models correspond to families that own castles.
    A House has the following attributes that appear on its page:
    - Name
    - Words
    - Location (ForeignKey Region)
    - Castle Name (ForeignKey Castle)
    - Description
    - People (ForeignKey Person)
    """
    # name
    house_id    = models.CharField(max_length=200, null=True)
    name        = models.CharField(max_length=200, null=True)

    # famous expressions
    words       = models.CharField(max_length=300, null=True)
    #sigil       = models.CharField(max_length=300, null=True)

    # the name of their castle
    castles_controlled = models.ManyToManyField(Castle, blank=True, related_name='house_castles_controlled')
    former_castles_controlled = models.ManyToManyField(Castle, blank=True, related_name='house_former_castles_controlled')

    # brief description
    description = models.TextField(null=True)

    # people in this House
    members     = models.ManyToManyField(Person, blank=True, related_name='house_family_members')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Author(models.Model) :
    """
    Author models correspond to each of the five team members
    that are building this website for cs373.
    An Author has the following attributes that appear on the about page:
    - Name
    - Bio
    - Responsibilities
    - Num Commits
    - Num Issues 
    - Num Unit Tests 
    """
    # name
    author_id        = models.CharField(max_length=200, null=True)
    first_name       = models.CharField(max_length=200, null=True)
    last_name        = models.CharField(max_length=200, null=True)

    # bio
    bio              = models.TextField(null=True)

    # major responsibilities
    responsibilities = models.TextField(null=True)

    # statistics
    num_commits      = models.IntegerField(null=True)
    num_issues       = models.IntegerField(null=True)
    num_unit_tests   = models.IntegerField(null=True)

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ('last_name',)
    
        
