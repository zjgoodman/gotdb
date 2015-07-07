#!/usr/bin/env python3

# -------
# imports
# -------

import json
import requests
from django.test import TestCase
from . import models

class GOT_Tests (TestCase):

    # Person(first_name, last_name, titles, status, bio)
    def test_person_1 (self):
        person 		= models.Person('Eddard',
            'Stark',
            'Lord of Winterfell',
            'Dead',
            'Neds bio')
        first_name 	= person.get_first_name()
        last_name 	= person.get_last_name()
        titles 		= person.get_titles()
        status 		= person.get_status()
        bio 		= person.get_bio()
        string      = person.__string__()

        self.assertEqual(first_name, 'Eddard')
        self.assertEqual(last_name,  'Stark')
        self.assertEqual(titles,     'Lord of Winterfell')
        self.assertEqual(status, 	 'Dead')
        self.assertEqual(bio,        'Neds bio')
        self.assertEqual(string, 	 'Eddard Stark')

    def test_person_2 (self):
        person 		= models.Person('Robert',
            'Baratheon',
            'Lord of the Seven Kingdoms',
            'Dead',
            'Roberts bio')
        first_name 	= person.get_first_name()
        last_name 	= person.get_last_name()
        titles 		= person.get_titles()
        status 		= person.get_status()
        bio 		= person.get_bio()
        string      = person.__string__()

        self.assertEqual(first_name, 'Robert')
        self.assertEqual(last_name,  'Baratheon')
        self.assertEqual(titles,     'Lord of the Seven Kingdoms')
        self.assertEqual(status, 	 'Dead')
        self.assertEqual(bio,        'Roberts bio')
        self.assertEqual(string, 	 'Robert Baratheon')

    def test_person_3 (self):
        person 		= models.Person('Tywin', Lannister',
            'Lord of Casterly Rock',
            'Dead',
            'Tywins bio')
        first_name 	= person.get_first_name()
        last_name 	= person.get_last_name()
        titles 		= person.get_titles()
        status 		= person.get_status()
        bio 		= person.get_bio()
        string      = person.__string__()

        self.assertEqual(first_name, 'Tywin')
        self.assertEqual(last_name,  'Lannister')
        self.assertEqual(titles,     'Lord of Casterly Rock')
        self.assertEqual(status, 	 'Dead')
        self.assertEqual(bio,        'Tywins bio')
        self.assertEqual(string, 	 'Tywin Lannister')

    # # Region(name, capitol, ruling family, description, history)
    # def test_region_1 (self):
    #     region = models.Region('The North',
    #         'Winterfell',
    #         'Starks',
    #         'Description',
    #         'History')
    #     name 			= region.get_name()
    #     capitol 		= region.get_capitol()
    #     ruling_family 	= region.get_ruling_family()
    #     description 	= region.get_description()
    #     history 		= region.get_history()
    #
    #     self.assertEqual(name,			'The North')
    #     self.assertEqual(capitol,		'Winterfell')
    #     self.assertEqual(ruling_family,	'Starks')
    #     self.assertEqual(description,	'Description')
    #     self.assertEqual(history,		'History')
    #
    # def test_region_2 (self):
    #     region = models.Region('The Stormlands',
    #         'Storm\'s end',
    #         'Baratheons',
    #         'Description',
    #         'History')
    #     name 			= region.get_name()
    #     capitol 		= region.get_capitol()
    #     ruling_family 	= region.get_ruling_family()
    #     description 	= region.get_description()
    #     history 		= region.get_history()
    #
    #     self.assertEqual(name,			'The Stormlands')
    #     self.assertEqual(capitol,		'Storm\'s end')
    #     self.assertEqual(ruling_family,	'Baratheons')
    #     self.assertEqual(description,	'Description')
    #     self.assertEqual(history,		'History')
    #
    # def test_region_3 (self):
    #     region = models.Region('The Westerlands',
    #         'Casterly Rock',
    #         'Lannisters',
    #         'Description',
    #         'History')
    #     name 			= region.get_name()
    #     capitol 		= region.get_capitol()
    #     ruling_family 	= region.get_ruling_family()
    #     description 	= region.get_description()
    #     history 		= region.get_history()
    #
    #     self.assertEqual(name,			'The Westerlands')
    #     self.assertEqual(capitol,		'Casterly Rock')
    #     self.assertEqual(ruling_family,	'Lannisters')
    #     self.assertEqual(description,	'Description')
    #     self.assertEqual(history,		'History')
    #
    #
    # # Caslte(Name, Location, Ruling Family, Description, History)
    # def test_castle_1 (self):
    #     castle = models.Castle('Winterfell',
    #         'The North',
    #         'Stark'
    #         'Description',
    #         'History')
    #     name 			= castle.get_name()
    #     location 		= castle.get_location()
    #     ruling_family 	= castle.get_ruling_family()
    #     description 	= region.get_description()
    #     history 		= region.get_history()
    #
    #     self.assertEqual(name,			'Winterfell')
    #     self.assertEqual(location,		'The North')
    #     self.assertEqual(ruling_family,	'Stark')
    #     self.assertEqual(description,	'Description')
    #     self.assertEqual(history,		'History')
    #
    # def test_castle_2 (self):
    #     castle = models.Castle('Storm\'s End',
    #         'The Stormlands',
    #         'Baratheon'
    #         'Description',
    #         'History')
    #     name 			= castle.get_name()
    #     location 		= castle.get_location()
    #     ruling_family 	= castle.get_ruling_family()
    #     description 	= region.get_description()
    #     history 		= region.get_history()
    #
    #     self.assertEqual(name,			'Storm\'s End')
    #     self.assertEqual(location,		'The Stormlands')
    #     self.assertEqual(ruling_family,	'Baratheon')
    #     self.assertEqual(description,	'Description')
    #     self.assertEqual(history,		'History')
    #
    # def test_castle_3 (self):
    #     castle = models.Castle('Casterly Rock',
    #         'The Westerlands',
    #         'Lannister'
    #         'Description',
    #         'History')
    #     name 			= castle.get_name()
    #     location 		= castle.get_location()
    #     ruling_family 	= castle.get_ruling_family()
    #     description 	= region.get_description()
    #     history 		= region.get_history()
    #
    #     self.assertEqual(name,			'Casterly Rock')
    #     self.assertEqual(location,		'The Westerlands')
    #     self.assertEqual(ruling_family,	'Lannister')
    #     self.assertEqual(description,	'Description')
    #     self.assertEqual(history,		'History')

class GOT_API_Tests (TestCase):
    url = "http://127.0.0.1:8000"

    def test_api_get_person (self):
        """
        Doing an http get on person 'Ned Stark'.
        Expecting a response with a json object
        containing Ned Starks data members
        """
        response = requests.get(self.url + '/content/api/people/')
        self.assertEqual(response.status_code, 200)
        actual = response.json()  # convert response to json obj
        expected = [{"id":1,"first_name":"Ned","last_name":"Stark","status":"Dead","bio":"Ned is cool"},{"id":2,"first_name":"Robert","last_name":"Baratheon","status":"Dead","bio":"He loves women"},{"id":3,"first_name":"Tywin","last_name":"Lannister","status":"Dead","bio":"Tywin is (was) pretty scary"}]
        self.assertEqual(actual, expected)

    def test_api_get_castle (self):
        """
        Doing an http get on person 'Ned Stark'.
        Expecting a response with a json object
        containing Ned Starks data members
        """
        response = requests.get(self.url + '/content/api/castles/')
        self.assertEqual(response.status_code, 200)
        actual = response.json()  # convert response to json obj
        expected = [{"id":2,"name":"Casterly Rock","region_name":2,"ruling_lord":3,"description":"The seat of house Lannister"},{"id":3,"name":"Storm's End","region_name":3,"ruling_lord":2,"description":"The seat of house Baratheon"},{"id":1,"name":"Winterfell","region_name":1,"ruling_lord":1,"description":"The seat of house Stark"}]
        self.assertEqual(actual, expected)

    def test_api_get_regions (self):
        """
        Doing an http get on person 'Ned Stark'.
        Expecting a response with a json object
        containing Ned Starks data members
        """
        response = requests.get(self.url + '/content/api/regions/')
        self.assertEqual(response.status_code, 200)
        actual = response.json()  # convert response to json obj
        expected = [{"id":3,"name":"Stormlands","capital_name":3,"ruling_lord":2,"description":"The Baratheon lands."},{"id":1,"name":"The North","capital_name":1,"ruling_lord":1,"description":"A big fancy place"},{"id":2,"name":"Westerlands","capital_name":2,"ruling_lord":3,"description":"The Lannister lands"}]
        self.assertEqual(actual, expected)

