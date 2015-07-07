#!/usr/bin/env python3

# -------
# imports
# -------

import json
import requests
from django.test import TestCase

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

