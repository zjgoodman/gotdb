#!/usr/bin/env python3

# -------
# imports
# -------

import json
import requests

from io       import StringIO
from django.test import TestCase

from .proj3site/populate_content import models



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
		first_name 	= Person.objects.get(last_name__exact=last_name)
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
		person 		= models.Person('Tywin',
			'Lannister',
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

	# Region(name, capitol, ruling family, description, history)
	def test_region_1 (self):
		region = models.Region('The North',
			'Winterfell',
			'Starks',
			'Description',
			'History')
		name 			= region.get_name()
		capitol 		= region.get_capitol()
		ruling_family 	= region.get_ruling_family()
		description 	= region.get_description()
		history 		= region.get_history()

		self.assertEqual(name,			'The North')
		self.assertEqual(capitol,		'Winterfell')
		self.assertEqual(ruling_family,	'Starks')
		self.assertEqual(description,	'Description')
		self.assertEqual(history,		'History')

	def test_region_2 (self):
		region = models.Region('The Stormlands',
			'Storm\'s end',
			'Baratheons',
			'Description',
			'History')
		name 			= region.get_name()
		capitol 		= region.get_capitol()
		ruling_family 	= region.get_ruling_family()
		description 	= region.get_description()
		history 		= region.get_history()

		self.assertEqual(name,			'The Stormlands')
		self.assertEqual(capitol,		'Storm\'s end')
		self.assertEqual(ruling_family,	'Baratheons')
		self.assertEqual(description,	'Description')
		self.assertEqual(history,		'History')

	def test_region_3 (self):
		region = models.Region('The Westerlands',
			'Casterly Rock',
			'Lannisters',
			'Description',
			'History')
		name 			= region.get_name()
		capitol 		= region.get_capitol()
		ruling_family 	= region.get_ruling_family()
		description 	= region.get_description()
		history 		= region.get_history()

		self.assertEqual(name,			'The Westerlands')
		self.assertEqual(capitol,		'Casterly Rock')
		self.assertEqual(ruling_family,	'Lannisters')
		self.assertEqual(description,	'Description')
		self.assertEqual(history,		'History')


	# Caslte(Name, Location, Ruling Family, Description, History)
	def test_castle_1 (self):
		castle = models.Castle('Winterfell',
			'The North',
			'Stark'
			'Description',
			'History')
		name 			= castle.get_name()
		location 		= castle.get_location()
		ruling_family 	= castle.get_ruling_family()
		description 	= region.get_description()
		history 		= region.get_history()

		self.assertEqual(name,			'Winterfell')
		self.assertEqual(location,		'The North')
		self.assertEqual(ruling_family,	'Stark')
		self.assertEqual(description,	'Description')
		self.assertEqual(history,		'History')

	def test_castle_2 (self):
		castle = models.Castle('Storm\'s End',
			'The Stormlands',
			'Baratheon'
			'Description',
			'History')
		name 			= castle.get_name()
		location 		= castle.get_location()
		ruling_family 	= castle.get_ruling_family()
		description 	= region.get_description()
		history 		= region.get_history()

		self.assertEqual(name,			'Storm\'s End')
		self.assertEqual(location,		'The Stormlands')
		self.assertEqual(ruling_family,	'Baratheon')
		self.assertEqual(description,	'Description')
		self.assertEqual(history,		'History')

	def test_castle_3 (self):
		castle = models.Castle('Casterly Rock',
			'The Westerlands',
			'Lannister'
			'Description',
			'History')
		name 			= castle.get_name()
		location 		= castle.get_location()
		ruling_family 	= castle.get_ruling_family()
		description 	= region.get_description()
		history 		= region.get_history()

		self.assertEqual(name,			'Casterly Rock')
		self.assertEqual(location,		'The Westerlands')
		self.assertEqual(ruling_family,	'Lannister')
		self.assertEqual(description,	'Description')
		self.assertEqual(history,		'History')


	# ---------------------------------------------------
	#					Api tests. 
	# ---------------------------------------------------

	url = "http://104.130.27.102:8000/"

	def test_api_get_person (self):
		"""
		Doing an http get on person 'Ned Stark'. 
		Expecting a response with a json object
		containing Ned Starks data members
		"""
		response = requests.get(self.url + 'people/Ned_Stark')
		self.assertEqual(response.status_code, 200)
		actual = response.json() #convert response to json obj
		expected = [{'Name':'Ned Stark', 
			'Title':'King of the North',
			'Status':'Dead',
			'Bio':'Neds bio',}]
		self.assertEqual(actual, expected)

	def test_api_get_region (self):
		"""
		Doing an http get on region 'The North'
		Expecting a response containing data
		related to this region.
		"""
		response = requests.get(self.url + 'region/The_North')
		self.assertEqual(response.status_code, 200)
		actual = response.json() #convert response to json obj
		expected = [{'Name':'The North',
			'Capitol':'Winterfell',
			'Ruling Family':'Stark',
			'Description':'Description',
			'History':'History'}]
		self.assertEqual(actual, expected)

	def test_api_get_castle (self):
		"""
		Doing an http get on castle 'Winterfell'
		Expecting a response containing data
		related to this castle.
		"""
		response = requests.get(self.url + 'castle/Winterfell')
		self.assertEqual(response.status_code, 200)
		actual = response.json() #convert response to json obj
		expected = [{'Name':'Winterfell',
			'Location':'The North',
			'Ruling Family':'Stark',
			'Description':'Description',
			'History':'History'}]
		self.assertEqual(actual, expected)