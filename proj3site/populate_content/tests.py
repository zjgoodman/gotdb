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



        self.region = Region.objects.create(name="it has castles",
                                            capital_name=Castle.objects.create(name='whatever'),
                                            ruling_house=House.objects.create(name='that one house'),
                                            description='may the lord bless your soul')

    def test_person_names_1(self):
        """
        Testing Person Models
        Create and store Person model
        check for correct output.
        """

        self.assertEqual(self.person.first_name, 'Eddard')
        self.assertEqual(self.person.last_name,  'Stark')
        self.assertEqual(self.person.__str__(), "Eddard Stark")

    def test_region_names_1(self):
        """
        Testing region Models
        Create and store Region model
        check for correct output.
        """
        self.assertEqual(self.region.__str__(), 'it has castles')
        self.assertEqual(self.region.capital_name.__str__(), 'whatever')
        self.assertEqual(self.region.ruling_house.__str__(), 'that one house')
        self.assertEqual(self.region.description, 'may the lord bless your soul')


class GOT_API_Tests (TestCase):

    url = "http://104.130.27.102:8000" # rackspace
    #url  = "http://127.0.0.1:8000"     # local

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