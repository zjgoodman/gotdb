#!/usr/bin/env python3

# -------
# imports
# -------

import json
import requests
from django.test import TestCase, Client
from rest_framework.test import APIClient
from .models import Person, Castle, Region, House
from django.core.urlresolvers import reverse


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
                                            region_from=self.regionTest,
                                            status='Dead',
                                            titles='Lord of Winterfell',
                                            bio='Neds bio')



        self.house = House.objects.create(name="Stark",
                                          words="Winter is coming?",
                                          description="my favorite obv",)

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


def make_person(p_id, first, last, description):
    return Person.objects.create(person_id=p_id, first_name=first, last_name=last, bio=description)


def make_region(r, n, h, d):
    return Region.objects.create(region_id=r, name=n, history=h, description=d)


def make_castle(c, n, h, d):
    return Castle.objects.create(castle_id=c, name=n, history=h, description=d)


def make_house(h, n, d):
    return House.objects.create(house_id=h, name=n, description=d)


class GOT_API_Tests (TestCase):
    def setUp(self):
        self.c = APIClient()
        # self.url  = "http://127.0.0.1:8000"     # local
        self.url = "http://housedowning-siteb.me" # rackspace


    def test_api_get_people(self):
        response = self.c.get('/api/people/')
        self.assertEqual(response.status_code, 200)

    def test_api_get_regions(self):
        response = self.c.get('/api/regions/')
        self.assertEqual(response.status_code, 200)

    def test_api_get_castles(self):
        response = self.c.get('/api/castles/')
        self.assertEqual(response.status_code, 200)

    def test_api_get_houses(self):
        response = self.c.get('/api/houses/')
        self.assertEqual(response.status_code, 200)

    def test_api_get_person_1(self):
        response = self.c.get(reverse('person_api_detail', args=["eddard_stark"]))
        self.assertEqual(response.status_code, 404)

    def test_api_get_person_2(self):
        make_person("eddard_stark", "Eddard", "Stark", "I don't care")
        response = self.c.get(reverse('person_api_detail', args=["eddard_stark"]))
        self.assertEqual(response.status_code, 200)

    def test_api_get_castle_1(self):
        response = self.c.get(reverse('castle_api_detail', args=["winterfell"]))
        self.assertEqual(response.status_code, 404)

    def test_api_get_castle_2(self):
        make_castle("winterfell", "Winterfell", "bloody", "has a cool tree")
        response = self.c.get(reverse('castle_api_detail', args=["winterfell"]))
        self.assertEqual(response.status_code, 200)

    def test_api_get_region_1(self):
        response = self.c.get(reverse('region_api_detail', args=["north"]))
        self.assertEqual(response.status_code, 404)

    def test_api_get_region_2(self):
        make_region("north", "North", "pretty old", "pretty cold")
        response = self.c.get(reverse('region_api_detail', args=["north"]))
        self.assertEqual(response.status_code, 200)

    def test_api_get_house_1(self):
        response = self.c.get(reverse('house_api_detail', args=["stark"]))
        self.assertEqual(response.status_code, 404)

    def test_api_get_house_2(self):
        make_house("stark", "House Stark", "They are all going to die")
        response = self.c.get(reverse('house_api_detail', args=["stark"]))
        self.assertEqual(response.status_code, 200)

    def test_api_get_person_live (self):
        """
        Doing an http get on people.
        Expecting a response with a json object
        containing a collection of each persons data members
        """
        response = requests.get(self.url + '/api/people/eddard_stark')
        self.assertEqual(response.status_code, 200)
        actual = response.json()  # convert response to json obj

        # check response
        self.assertEqual("Eddard", actual['first_name'])
        self.assertEqual("Stark", actual['last_name'])
        self.assertEqual("Deceased", actual['status'])

    def test_api_get_castle_live (self):
        """
        Doing an http get on castles.
        Expecting a response with a json object
        containing a collection of each castle data members
        """
        response = requests.get(self.url + '/api/castles/casterly_rock')
        self.assertEqual(response.status_code, 200)
        actual = response.json()  # convert response to json obj

        # check response
        self.assertEqual('casterly_rock', actual['castle_id'])
        self.assertEqual("Casterly Rock", actual["name"])

    def test_api_get_region_live(self):
        """
        Doing an http get on regions.
        Expecting a response with a json object
        containing a collection of each regions data members
        """
        response = requests.get(self.url + '/api/regions/stormlands')
        self.assertEqual(response.status_code, 200)
        actual = response.json()  # convert response to json obj

        # check response
        self.assertEqual("stormlands", actual["region_id"])
        self.assertEqual("The Stormlands", actual["name"])

    def test_api_get_house_live(self):
        """
        Doing an http get on houses.
        Expecting a response with a json object
        containing a collection of each houses data members
        """
        response = requests.get(self.url + '/api/houses/stark')
        self.assertEqual(response.status_code, 200)
        actual = response.json()  # convert response to json obj

        # check response
        self.assertEqual("stark", actual["house_id"])
        self.assertEqual("House Stark", actual["name"])
        self.assertEqual("Winter is Coming", actual["words"])


class GOT_Views_Tests (TestCase):
    def setUp(self):
        self.c = Client()

    def test_index_view(self):
        response = self.c.get(reverse('splash'))
        self.assertEqual(response.status_code, 200)

    def test_about_index_view(self):
        response = self.c.get(reverse('about_index'))
        self.assertEqual(response.status_code, 200)

    def test_person_index_view(self):
        response = self.c.get(reverse('person_index'))
        self.assertEqual(response.status_code, 200)

    def test_castle_index_view(self):
        response = self.c.get(reverse('castle_index'))
        self.assertEqual(response.status_code, 200)

    def test_region_index_view(self):
        response = self.c.get(reverse('region_index'))
        self.assertEqual(response.status_code, 200)

    def test_house_index_view(self):
        response = self.c.get(reverse('house_index'))
        self.assertEqual(response.status_code, 200)

    def test_person_detail_view_1(self):
        response = self.c.get(reverse('person_detail', args=["eddard_stark"]))
        self.assertEqual(response.status_code, 404)

    def test_person_detail_view_2(self):
        make_person("eddard_stark", "Eddard", "Stark", "I don't care")
        response = self.c.get(reverse('person_detail', args=["eddard_stark"]))
        self.assertEqual(response.status_code, 200)

    def test_region_detail_view_1(self):
        response = self.c.get(reverse('region_detail', args=["north"]))
        self.assertEqual(response.status_code, 404)

    def test_region_detail_view_2(self):
        make_region("north", "North", "pretty old", "pretty cold")
        response = self.c.get(reverse('region_detail', args=["north"]))
        self.assertEqual(response.status_code, 200)

    def test_castle_detail_view_1(self):
        response = self.c.get(reverse('castle_detail', args=["winterfell"]))
        self.assertEqual(response.status_code, 404)

    def test_castle_detail_view_2(self):
        make_castle("winterfell", "Winterfell", "bloody", "has a cool tree")
        response = self.c.get(reverse('castle_detail', args=["winterfell"]))
        self.assertEqual(response.status_code, 200)

    def test_house_detail_view_1(self):
        response = self.c.get(reverse('house_detail', args=["stark"]))
        self.assertEqual(response.status_code, 404)

    def test_house_detail_view_2(self):
        make_house("stark", "House Stark", "They are all going to die")
        response = self.c.get(reverse('house_detail', args=["stark"]))
        self.assertEqual(response.status_code, 200)

    def test_all_people_view(self):
        make_person("eddard_stark", "Eddard", "Stark", "I don't care")
        response = self.c.get(reverse('all_people_index'))
        self.assertEqual(response.status_code, 200)

    def test_all_castle_view(self):
        make_castle("winterfell", "Winterfell", "bloody", "has a cool tree")
        response = self.c.get(reverse('all_castles_index'))
        self.assertEqual(response.status_code, 200)

    def test_all_regions_view(self):
        make_region("north", "North", "pretty old", "pretty cold")
        response = self.c.get(reverse('all_regions_index'))
        self.assertEqual(response.status_code, 200)

    def test_all_houses_view(self):
        make_house("stark", "House Stark", "They are all going to die")
        response = self.c.get(reverse('all_houses_index'))
        self.assertEqual(response.status_code, 200)