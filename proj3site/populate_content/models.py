from django.db import models
from django.contrib.auth.models import User

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
    cause_of_death = models.CharField(max_length=200, null=True)
    killer         = models.ForeignKey('Person', null=True)

    # short biographical information
    bio            = models.TextField(null=True)

    def __str__(self):
        if not self.last_name :
            return self.first_name
        return self.first_name + " " + self.last_name

    def get_url(self):
        return "/people/" + self.person_id

    def get_id(self):
        return self.person_id

    def get_img(self):
        return "img/person/" + self.person_id + ".jpg"

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

    ruling_lord            = models.ForeignKey(Person, null=True)

    # information
    description   = models.TextField(null=True)
    history       = models.TextField(null=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return "/regions/" + self.region_id

    def get_id(self):
        return self.region_id

    def get_img(self):
        return "img/place/" + self.region_id + ".jpg"

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
    primary_house   = models.ForeignKey('House', null=True)
    # related houses
    previous_houses = models.ManyToManyField('House', blank=True, related_name='castle_previous_houses')
    
    # lords of the castle
    primary_lord    = models.ForeignKey(Person, null=True)
    previous_lords  = models.ManyToManyField(Person, blank=True, related_name='castle_previous_lords')

    # brief description
    description     = models.TextField(null=True)
    history         = models.TextField(null=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return "/castles/" + self.castle_id

    def get_id(self):
        return self.castle_id

    def get_img(self):
        return "img/place/" + self.castle_id + ".jpg"

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
    sigil       = models.CharField(max_length=300, null=True)

    # the name of their castle
    castles_controlled = models.ManyToManyField(Castle, blank=True, related_name='house_castles_controlled')
    former_castles_controlled = models.ManyToManyField(Castle, blank=True, related_name='house_former_castles_controlled')

    # brief description
    description = models.TextField(null=True)

    # people in this House
    members     = models.ManyToManyField(Person, blank=True, related_name='house_family_members')

    def __str__(self):
        return self.name

    def get_url(self):
        return "/houses/" + self.house_id

    def get_id(self):
        return self.house_id

    def get_img(self):
        return "img/house/" + self.house_id + ".jpg"

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

class Cities(models.Model) :
    """
    Cities models correspond to each of the three Cities containing the shelters
    that are in the GotoPaws database.
    A Cities object has the following attributes:
        "city_vet_url": "http://www.yelp.com/biz/san-francisco-pet-hospital-san-francisco",
        "city_country": "US",
        "city_state": "CA",
        "city_park_pic": "bootstrap-3.3.5-dist/img/Cities/san-franc_park.jpg", #NOT USING YET
        "city_groomer_url": "http://www.yelp.com/biz/san-francisco-pet-hospital-san-francisco",
        "city_park_url": "www.google.com",
        "city_name": "San Francisco",
        "city_vet_pic": "bootstrap-3.3.5-dist/img/Cities/san-franc_vet.jpg", #NOT USING YET
        "city_groomer_pic": "bootstrap-3.3.5-dist/img/Cities/san-franc_groomer.jpg",  #NOT USING YET
        "city_url": "City_SF.html", #NOT USING YET
        "city_pic": "bootstrap-3.3.5-dist/img/Cities/san-franc.jpg" #NOT USING YET
    """
    city_vet_url              = models.CharField(max_length=200, null=True)
    city_country            = models.CharField(max_length=200, null=True)
    city_state            = models.CharField(max_length=2, null=True)
    city_groomer_url            = models.CharField(max_length=200, null=True)
    city_park_url             = models.CharField(max_length=200, null=True)
    city_name             = models.CharField(max_length=200, null=True)
    city_pic             = models.CharField(max_length=200, null=True)
    city_url             = models.CharField(max_length=200, null=True)
    city_groomer_pic             = models.CharField(max_length=200, null=True)
    city_vet_pic             = models.CharField(max_length=200, null=True)
    city_park_pic             = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.city_name

    def get_id(self):
        return self.city_name + '_' + self.city_state

    class Meta:
        ordering = ('city_name',)

class Shelter(models.Model) :
    """
    Shelter models correspond to each of the three animal Shelters
    that are in the GotoPaws database.
    A Shelter object has the following attributes:
        "shelter_email"
        "shelter_city_url"
        "shelter_phone"
        "shelter_city"
        "shelter_url" NOT USING THIS YET!!!!!!!!!!!!!!!!!!!
        "shelter_state"
        "shelter_id"
        "shelter_pic" NOT USING THIS YET!!!!!!!!!
        "shelter_hours"
        "shelter_address"
        "shelter_name"
    """
    shelter_id              = models.CharField(max_length=200, null=True)
    shelter_name            = models.CharField(max_length=200, null=True)
    shelter_city            = models.CharField(max_length=200, null=True)
    shelter_address            = models.CharField(max_length=200, null=True)
    shelter_hours             = models.CharField(max_length=200, null=True)
    shelter_state             = models.CharField(max_length=2, null=True)
    shelter_phone           = models.CharField(max_length=200, null=True)
    shelter_email         = models.CharField(max_length=200, null=True)
    shelter_url         = models.CharField(max_length=200, null=True)
    shelter_pic         = models.CharField(max_length=200, null=True)

    # Here is where things may need to change. not sure.
    shelter_city_url            = models.ForeignKey('Cities', null=True)

    def __str__(self):
        return self.shelter_name

    def get_id(self):
        return self.shelter_id

    class Meta:
        ordering = ('shelter_name',)

class Pets(models.Model) :
    """
    Pets models correspond to each of the three pets
    that are in the GotoPaws database.
    A Pets object has the following attributes:
        "pet_size"
        "pet_shelter",
        "pet_pic_large"
        "pet_pic_url"
        "pet_url" NOT USING THIS ONE!!!!!!!!!!!!
        "pet_age"
        "pet_sex"
        "pet_shelter_url"
        "pet_breed"
        "pet_name"
        "pet_city_url"
        "pet_id"
        "pet_city"
    """
    pet_id              = models.CharField(max_length=200, null=True)
    pet_shelter         = models.CharField(max_length=200, null=True)
    pet_name            = models.CharField(max_length=200, null=True)
    pet_city            = models.CharField(max_length=200, null=True)
    pet_size            = models.CharField(max_length=200, null=True)
    pet_age             = models.CharField(max_length=200, null=True)
    pet_sex             = models.CharField(max_length=200, null=True)
    pet_breed           = models.CharField(max_length=200, null=True)
    pet_pic_url         = models.CharField(max_length=200, null=True)
    pet_pic_large       = models.CharField(max_length=200, null=True) #the picture is within bootstrap/img.

    # Here is where things may need to change. not sure.
    pet_city_url            = models.ForeignKey('Cities', null=True)
    pet_shelter_url         = models.ForeignKey('Shelter', null=True)

    def __str__(self):
        return self.pet_name

    def get_id(self):
        return self.pet_id

    class Meta:
        ordering = ('pet_name',)



