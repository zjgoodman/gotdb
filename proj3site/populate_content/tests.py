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
        self.castleTest = Castle.objects.create(name="Castle Black")
        self.personTest = Person.objects.create(last_name='Stark', first_name='Eddard')
        self.houseTest = House.objects.create(name="Stark")
        self.regionTest = Region.objects.create(name="it has castles")

        self.castle = Castle.objects.create(name="Castle Black",
                                            region_name=self.regionTest,
                                            description="Meh, it's pretty")

        self.person = Person.objects.create(last_name='Stark',
                                            first_name='Eddard',
                                            # houses=self.houseTest,
                                            region_from=self.regionTest,
                                            status='Dead',
                                            titles='Lord of Winterfell',
                                            bio='Neds bio')



        self.house = House.objects.create(name="Stark",
                                          words="Winter is coming?",
                                          description="my favorite obv",
                                          #members=self.personTest
                                          )

        self.region = Region.objects.create(name="it has castles",
                                            capital_name=self.castleTest,
                                            ruling_house=self.houseTest,
                                            description='may the lord bless your soul')
    """
    Testing the string method of each model
    """

    def test_person_names(self):
        """
        Testing Person names
        Create and store Person model
        check for correct output.
        """

        self.assertEqual(self.person.first_name, 'Eddard')
        self.assertEqual(self.person.last_name,  'Stark')
        self.assertEqual(self.person.__str__(), "Eddard Stark")

    def test_region_names(self):
        """
        Testing region names
        check name matches output of __str__() method.
        """
        self.assertEqual(self.region.name, 'it has castles')
        self.assertEqual(self.region.__str__(), 'it has castles')

    def test_house_names(self):
        """
        Testing house names
        check name matches output of __str__() method.
        """
        self.assertEqual(self.house.name, 'Stark')
        self.assertEqual(self.house.__str__(), 'Stark')

    def test_castle_names(self):
        """
        Testing castle names
        check name matches output of __str__() method.
        """
        self.assertEqual(self.castle.name, 'Castle Black')
        self.assertEqual(self.castle.__str__(), 'Castle Black')

    """
    Testing the builtin foreign key relations in each model
    """

    def test_person_relations(self):
        """
        Testing person Model
        check that each underlying model matches the expected output
        """

        self.assertEqual(self.person.region_from.__str__(), 'it has castles')
        self.assertEqual(self.person.titles, 'Lord of Winterfell')

    def test_castle_relations(self):
        """
        Testing castle Model
        check that each field matches the expected output
        (No relations in this model)
        """
        self.assertEqual(self.castle.region_name.__str__(), 'it has castles')
        self.assertEqual(self.castle.description, "Meh, it's pretty")

    def test_region_relations(self):
        """
        Testing region Model
        check that each underlying model matches the expected output
        """
        self.assertEqual(self.region.capital_name.__str__(), 'Castle Black')
        self.assertEqual(self.region.ruling_house.__str__(), 'Stark')
        self.assertEqual(self.region.description.__str__(), 'may the lord bless your soul')

    def test_house_relations(self):
        """
        Testing house Model
        check that each underlying model matches the expected output
        """
        self.assertEqual(self.house.words, "Winter is coming?")



# class GOT_API_Tests (TestCase):
#
#     #url = "http://104.130.27.102:8000" # rackspace
#     url  = "http://127.0.0.1:8000"     # local
#
#     def test_api_get_person (self):
#         """
#         Doing an http get on people.
#         Expecting a response with a json object
#         containing a collection of each persons data members
#         """
#         response = requests.get(self.url + '/content/api/people/eddard_stark')
#         self.assertEqual(response.status_code, 200)
#         actual = response.json()  # convert response to json obj
#
#         #check response
#         self.assertEqual("Eddard", actual['first_name'])
#         self.assertEqual("Stark", actual['last_name'])
#         self.assertEqual("Deceased", actual['status'])
#
#     def test_api_get_castle (self):
#         """
#         Doing an http get on castles.
#         Expecting a response with a json object
#         containing a collection of each castle data members
#         """
#         response = requests.get(self.url + '/content/api/castles/casterly_rock')
#         self.assertEqual(response.status_code, 200)
#         actual = response.json()  # convert response to json obj
#
#         # check response
#         self.assertEqual('casterly_rock', actual['castle_id'])
#         self.assertEqual("Casterly Rock", actual["name"])
#
#     def test_api_get_regions (self):
#         """
#         Doing an http get on regions.
#         Expecting a response with a json object
#         containing a collection of each regions data members
#         """
#         response = requests.get(self.url + '/content/api/regions/stormlands')
#         self.assertEqual(response.status_code, 200)
#         actual = response.json()  # convert response to json obj
#
#         # check response
#         self.assertEqual("stormlands", actual["region_id"])
#         self.assertEqual("The Stormlands", actual["name"])
#
#     def test_api_get_houses (self):
#         """
#         Doing an http get on houses.
#         Expecting a response with a json object
#         containing a collection of each houses data members
#         """
#         response = requests.get(self.url + '/content/api/houses/stark')
#         self.assertEqual(response.status_code, 200)
#         actual = response.json()  # convert response to json obj
#
#         # check response
#         self.assertEqual("stark", actual["house_id"])
#         self.assertEqual("House Stark", actual["name"])
#         self.assertEqual("Winter is Coming", actual["words"])