#!/usr/bin/env python3

# -------
# imports
# -------

import json
import requests
from django.test import TestCase
from .models import Person, Castle, Region, House


class GOT_Tests (TestCase):
    def setUp(self):
        self.person = Person.objects.create(last_name='Stark',
                        first_name='Eddard',
                        status='Dead',
                        titles='Lord of Winterfell',
                        bio='Neds bio')

        # region = Person.objects.create(name='The North',
        #                        capital_name=models.Castle(self, name='whatever'),
        #                        ruling_house=models.House(self, name='that one house'),
        #                        ruling_lord=models.Person(self, first_name="evil guy", last_name="prob"),
        #                        description='may the lord bless your soul')

    def test_names_1(self):
        """
        Testing Person Models
        Create and store Person model
        check for correct output.
        """

        self.assertEqual(self.person.first_name, 'Eddard')
        self.assertEqual(self.person.last_name,  'Stark')
    #
    # def test_person_2(self):
    #     """
    #     Testing Person Models
    #     Create and store Person model (move input around)
    #     check for correct output.
    #     """
    #     person = Person(last_name='Stark',
    #                            first_name='Eddard',
    #                            status='Dead',
    #                            titles='Lord of Winterfell',
    #                            bio='Neds bio')
    #
    #     person2 = models.Person(last_name='Stark',
    #                            first_name='Eddard',
    #                            status='Dead',
    #                            titles='Lord of Winterfell',
    #                            bio='Neds bio')
    #
    #     first_name = person.first_name
    #     last_name = person.last_name
    #     titles = person.titles
    #     status = person.status
    #     bio = person.bio
    #
    #     self.assertEqual(first_name, 'Eddard')
    #     self.assertEqual(last_name,  'Stark')
    #     self.assertEqual(titles,     'Lord of Winterfell')
    #     self.assertEqual(status, 	 'Dead')
    #     self.assertEqual(bio,        'Neds bio')
    #     self.assertEqual(person, person2)
    #
    # def test_person_3(self):
    #     """
    #     Testing Person Models
    #     Get the contents of the __str__ method
    #     check for correct output (persons name).
    #     """
    #     person = models.Person(first_name='Eddard',
    #                            last_name='Stark',
    #                            titles='Lord of Winterfell',
    #                            status='Dead',
    #                            bio='Neds bio')
    #
    #     self.assertEqual(str(person), "Eddard Stark")
    #
    # def test_region_1(self):
    #     """
    #     Testing region Models
    #     Create and store Region model
    #     check for correct output.
    #     """
    #     region = models.Region(name='The North',
    #                            capital_name=models.Castle(self, name='whatever'),
    #                            ruling_house=models.House(self, name='that one house'),
    #                            ruling_lord=models.Person(self, first_name="evil guy", last_name="prob"),
    #                            description='may the lord bless your soul')
    #     name = region.name
    #     capital = region.capital_name
    #     house = region.ruling_house
    #     lord = region.ruling_lord
    #     bio = region.description
    #
    #     self.assertEqual(name, 'The North')
    #     self.assertEqual(capital,  models.Castle(self, name='whatever'))
    #     self.assertEqual(house,     models.House(self, name='that one house'))
    #     self.assertEqual(lord, 	 models.Person(self, first_name="evil guy", last_name="prob"))
    #     self.assertEqual(bio,        'may the lord bless your soul')
    #
    # def test_region_2(self):
    #     """
    #     Testing region Models
    #     Create and store Region model
    #     check for correct output.
    #     """
    #     region = models.Region(name='The North',
    #                            ruling_lord=models.Person(self, first_name="evil guy", last_name="prob"),
    #                            ruling_house=models.House(self, name='that one house'),
    #                            capital_name=models.Castle(self, name='whatever'),
    #                            description='may the lord bless your soul')
    #     name = region.name
    #     capital = region.capital_name
    #     house = region.ruling_house
    #     lord = region.ruling_lord
    #     bio = region.description
    #
    #     self.assertEqual(name, 'The North')
    #     self.assertEqual(capital,  models.Castle(self, name='whatever'))
    #     self.assertEqual(house,     models.House(self, name='that one house'))
    #     self.assertEqual(lord, 	 models.Person(self, first_name="evil guy", last_name="prob"))
    #     self.assertEqual(bio,        'may the lord bless your soul')
    #
    # def test_region_3(self):
    #     """
    #     Testing region Models
    #     Create and store Region model
    #     check for correct output.
    #     """
    #     region = models.Region(name='The North',
    #                            capital_name=models.Castle(self, name='whatever'),
    #                            ruling_house=models.House(self, name='that one house'),
    #                            ruling_lord=models.Person(self, first_name="evil guy", last_name="prob"),
    #                            description='may the lord bless your soul')
    #
    #     self.assertEqual(str(region), 'The North')
    #
    #
    # def test_castles_1(self):
    #     """
    #     Testing Castle Models
    #     Create and store Castle model
    #     check for correct output.
    #     """
    #     castle = models.Castle(name='The North',
    #                            region_name=models.Region(self, name='whatever'),
    #                            ruling_house=models.House(self, name='that one house'),
    #                            ruling_lord=models.Person(self, first_name="evil guy", last_name="prob"),
    #                            description='may the lord bless your soul')
    #     name = castle.name
    #     capital = castle.region_name
    #     house = castle.ruling_house
    #     lord = castle.ruling_lord
    #     bio = castle.description
    #
    #     self.assertEqual(name, 'The North')
    #     self.assertEqual(capital,  models.Region(self, name='whatever'))
    #     self.assertEqual(house,     models.House(self, name='that one house'))
    #     self.assertEqual(lord, 	 models.Person(self, first_name="evil guy", last_name="prob"))
    #     self.assertEqual(bio,        'may the lord bless your soul')
    #
    # def test_castles_2(self):
    #     """
    #     Testing Castle Models
    #     Create and store Castle model
    #     check for correct output.
    #     """
    #     castle = models.Castle(name='The North',
    #                            ruling_lord=models.Person(self, first_name="evil guy", last_name="prob"),
    #                            ruling_house=models.House(self, name='that one house'),
    #                            region_name=models.Region(self, name='whatever'),
    #                            description='may the lord bless your soul')
    #     name = castle.name
    #     capital = castle.region_name
    #     house = castle.ruling_house
    #     lord = castle.ruling_lord
    #     bio = castle.description
    #
    #     self.assertEqual(name, 'The North')
    #     self.assertEqual(capital,  models.Region(self, name='whatever'))
    #     self.assertEqual(house,     models.House(self, name='that one house'))
    #     self.assertEqual(lord, 	 models.Person(self, first_name="evil guy", last_name="prob"))
    #     self.assertEqual(bio,        'may the lord bless your soul')
    #
    # def test_castles_3(self):
    #     """
    #     Testing Castle Models
    #     Create and store Castle model
    #     check for correct output.
    #     """
    #     castle = models.Castle(name='The North',
    #                            region_name=models.Region(self, name='whatever'),
    #                            ruling_house=models.House(self, name='that one house'),
    #                            ruling_lord=models.Person(self, first_name="evil guy", last_name="prob"),
    #                            description='may the lord bless your soul')
    #
    #     self.assertEqual(str(castle), 'The North')
    #
    #
    # def test_House_1(self):
    #     """
    #     Testing house Models
    #     Create and store house model
    #     check for correct output.
    #     """
    #     house = models.House(name='The North',
    #                          words='some words',
    #                          region_name=models.Region(self, name='whatever'),
    #                          castle_name=models.Castle(self, name='that one place'),
    #                          description='may the lord bless your soul')
    #     name = house.name
    #     words = house.words
    #     region = house.region_name
    #     castle = house.castle_name
    #     bio = house.description
    #
    #     self.assertEqual(name, 'The North')
    #     self.assertEqual(words, 'some words')
    #     self.assertEqual(region,     models.Region(self, name='whatever'))
    #     self.assertEqual(castle, 	 models.Castle(self, name='that one place'))
    #     self.assertEqual(bio,        'may the lord bless your soul')
    #
    # def test_House_2(self):
    #     """
    #     Testing house Models
    #     Create and store house model
    #     check for correct output.
    #     """
    #     house = models.House(name='The North',
    #                          region_name=models.Region(self, name='whatever'),
    #                          words='some words',
    #                          castle_name=models.Castle(self, name='that one place'),
    #                          description='may the lord bless your soul')
    #     name = house.name
    #     words = house.words
    #     region = house.region_name
    #     castle = house.castle_name
    #     bio = house.description
    #
    #     self.assertEqual(name, 'The North')
    #     self.assertEqual(words, 'some words')
    #     self.assertEqual(region,     models.Region(self, name='whatever'))
    #     self.assertEqual(castle, 	 models.Castle(self, name='that one place'))
    #     self.assertEqual(bio,        'may the lord bless your soul')
    #
    # def test_House_3(self):
    #     """
    #     Testing house Models
    #     Create and store house model
    #     check for correct output.
    #     """
    #     house = models.House(name='The North',
    #                          words='some words',
    #                          region_name=models.Region(self, name='whatever'),
    #                          castle_name=models.Castle(self, name='that one place'),
    #                          description='may the lord bless your soul')
    #
    #     self.assertEqual(str(house), 'The North')


class GOT_API_Tests (TestCase):

    # url = "http://104.130.27.102:8000" # rackspace
    url  = "http://127.0.0.1:8000"     # local

    def test_api_get_person (self):
        """
        Doing an http get on people.
        Expecting a response with a json object
        containing a collection of each persons data members
        """
        response = requests.get(self.url + '/content/api/people/eddard_stark')
        self.assertEqual(response.status_code, 200)
        actual = response.json()  # convert response to json obj

        #check response
        self.assertEqual("Eddard", actual['first_name'])
        self.assertEqual("Stark", actual['last_name'])
        self.assertEqual("Deceased", actual['status'])

    def test_api_get_castle (self):
        """
        Doing an http get on castles.
        Expecting a response with a json object
        containing a collection of each castle data members
        """
        response = requests.get(self.url + '/content/api/castles/casterly_rock')
        self.assertEqual(response.status_code, 200)
        actual = response.json()  # convert response to json obj

        # check response
        self.assertEqual('casterly_rock', actual['castle_id'])
        self.assertEqual("Casterly Rock", actual["name"])

    def test_api_get_regions (self):
        """
        Doing an http get on regions.
        Expecting a response with a json object
        containing a collection of each regions data members
        """
        response = requests.get(self.url + '/content/api/regions/stormlands')
        self.assertEqual(response.status_code, 200)
        actual = response.json()  # convert response to json obj

        # check response
        self.assertEqual("stormlands", actual["region_id"])
        self.assertEqual("The Stormlands", actual["name"])

    def test_api_get_houses (self):
        """
        Doing an http get on houses.
        Expecting a response with a json object
        containing a collection of each houses data members
        """
        response = requests.get(self.url + '/content/api/houses/stark')
        self.assertEqual(response.status_code, 200)
        actual = response.json()  # convert response to json obj

        # check response
        self.assertEqual("stark", actual["house_id"])
        self.assertEqual("House Stark", actual["name"])
        self.assertEqual("Winter is Coming", actual["words"])