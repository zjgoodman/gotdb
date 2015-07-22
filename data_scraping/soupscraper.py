import urllib2
from bs4 import BeautifulSoup
# from types import *

# testpage = urllib2.urlopen('http://gameofthrones.wikia.com/wiki/Category:Noble_houses')
# soup = BeautifulSoup(testpage.read())
# houses = {}
# for link in soup.find_all('a'):
# 	subject = link.get('title')
# 	try:
# 		if subject.startswith("House"):
# 			if subject.count(' ') == 1:
# 				houses[subject] = 0
# 	except:
# 		pass
# print(houses)

# for house in houses:
# 	if not house.get():
#
hdr = {'User-Agent': 'Mozilla/5.0'}  #for permissions

#using Westeros.org
#finds and scrapes info on all people listed in string
# print("People:\n")
# for name in ('Eddard_Stark', 'Tywin_Lannister', 'Robert_Baratheon', 'Daenerys_Targaryen', 'Jon_Snow', 'Sansa_Stark', 'Arya_Stark', 'Stannis_Baratheon', 'Tyrion_Lannister', 'Theon_Grejoy', 'Joffrey_Baratheon', 'Ramsay_Bolton', 'Cersei_Lannister', 'Bran_Stark', 'Margaery_Tyrell', 'Melisandre_of_Asshai', 'Daario_Naharis', 'Jaime_Lannister', 'Robb_Stark', 'Jorah_Mormont', 'Petyr_Baelish', 'Tommen_Baratheon', 'Sandor_Clegane', 'Jaqen_Hghar', 'Gendry', 'Khal_Drogo', 'Brienne_of_Tarth', 'Ygritte', 'Roose_Bolton', 'Catelyn_Stark', 'Varys', 'Bronn', 'Viserys_Targaryen', 'Shae', 'Talisa_Stark', 'Ellaria_Sand', 'Jeor_Mormont', 'Samwell_Tarly', 'Davos_Seaworth', 'Gilly', 'Tormund', 'Missandei'):
# 	# name = 'Eddard_Stark'
# 	site = 'http://www.westeros.org/GoT/Characters/Entry/' + name
# 	req = urllib2.Request(site, headers=hdr)
# 	page = urllib2.urlopen(req)
# 	soup = BeautifulSoup(page)
# 	print(name + ':')
# 	data = soup.find(id="Wrapper").find(id = "Main").find(id = "MainMiddle").find(id = "MainMiddleInner")
# 	for line in data.find('div', attrs={'class': 'CharActor'}):
# 		try:
# 			if line[1:].startswith("Played"): #find line with actor name
# 				print(line[1:-1])
# 		except:
# 			pass
# 	# print(data.find('div', attrs={'class': 'CharActor'})[10:-4])
# 	for parag in data.find_all('p'):
# 		parag = str(parag)
# 		#Parse out any '<' or '>' and inbetween to remove ugly html
# 		while parag.find('<') != -1 and parag.find('>') != -1:
# 			start = parag.find('<')
# 			cut = start
# 			end = parag.find('>')

# 			while (start < end):
# 				start += 1
# 				if parag[start] == '<':
# 					cut = start
# 			parag = parag[:cut] + parag[end + 1:] #removed bracketed section
# 		print("<p>" + parag + "</p>")
# 	print('\n\n')

# using gameofthrones.wikia.com
# finds and scrapes info on all places and regions listed in string, places first
people = False
places = False
regions = False
houses = True
pcount = 0
skip = True
main_dict = []
print('[')
for place in (

	# ------
	# PEOPLE
	# ------

	# stark
	'Eddard_Stark', 'Jon_Snow', 'Sansa_Stark', 'Arya_Stark', 'Bran_Stark', 'Robb_Stark', 'Talisa_Stark', 'Catelyn_Stark', 'Benjen_Stark', 'Rickon_Stark', 'Hodor', 'Rodrik_Cassel',
	
	# lannister
	'Tywin_Lannister', 'Tyrion_Lannister', 'Cersei_Lannister', 'Jaime_Lannister', 'Lancel', 'Kevan_Lannister', 
	
	# targaryen
	'Daenerys_Targaryen', 'Viserys_Targaryen', 'Aemon',
	
	# bolton
	'Ramsay_Bolton', 'Roose_Bolton',
	
	# tyrell
	'Margaery_Tyrell', 'Loras_Tyrell', 'Olenna_Tyrell',
	
	# martell
	'Ellaria_Sand', 'Tyene_Sand', 'Oberyn_Martell', 'Doran_Martell', 'Nymeria_Sand', 'Obara_Sand',
	
	# clegane
	'Sandor_Clegane', 'Gregor_Clegane',
	
	# karstark
	'Rickard_Karstark',
	
	# umber
	'Greatjon_Umber',
	
	# frey
	'Walder_Frey', 'Roslin_Frey', 'Walda_Frey_(Fat_Walda)',
	
	# Arryn
	'Lysa_Arryn', 'Robin_Arryn', 'Jon_Arryn',
	
	# tully
	'Hoster_Tully', 'Brynden_Tully', 'Edmure_Tully',
	
	# baelish
	'Petyr_Baelish',
	
	# baratheon
	'Robert_Baratheon', 'Renly_Baratheon', 'Stannis_Baratheon', 'Joffrey_Baratheon', 'Tommen_Baratheon', 'Shireen_Baratheon', 'Myrcella_Baratheon', 'Selyse_Baratheon',
	
	# greyjoy
	'Balon_Greyjoy', 'Yara_Greyjoy', 'Theon_Greyjoy',
	
	# mormont
	'Jeor_Mormont', 'Jorah_Mormont',
	
	# tarly
	'Samwell_Tarly',
	
	# beyond the wall
	'Tormund', 'Alliser_Thorne', 'Mance_Rayder', 'Ygritte', 'Gilly', 'Janos_Slynt',
	
	# essos people
	'Daario_Naharis', 'Jaqen_H\'ghar', 'Drogo', 'Barristan_Selmy', 'Missandei', 'Grey_Worm',
	
	# no house
	'Melisandre', 'Davos_Seaworth', 'Gendry', 'Varys', 'Bronn', 'Shae', 'Brienne_of_Tarth', 'Meryn_Trant', 'Myranda', 'Podrick_Payne', 'High_Sparrow', 'Osha', 'Pycelle', 'Luwin',
	
	# -------
	# CASTLES
	# -------

	# 7 kingdoms
	'Winterfell', 'Storm\'s_End', 'Casterly_Rock', 'Sunspear',
	'Highgarden', 'The_Eyrie', 'Riverrun',

	# other westeros castles
	'Red_Keep',

	# north
	'Last_Hearth', 'Karhold', 'Moat_Cailin', 'The_Dreadfort', 'Castle_Black',

	'Clegane\'s_Keep', 'Evenfall_Hall', 'Harrenhal', 'Dragonstone', 'Pyke_(castle)',
	'The_Twins',

	# ------
	# CITIES
	# ------

	# westeros
	'King\'s_Landing', 

	# essos
	'Asshai', 'Volantis', 'Hellholt', 'Horn_Hill', 'Craster\'s_Keep', 'Naath',
	'Braavos', 'Vaes_Dothrak', 'Tyrosh', 'Lys', 'Lorath', 'Pentos', 'Astapor',
	'Meereen', 'Yunkai', 'Old_Valyria', 'Qarth',

	# -------
	# REGIONS
	# -------

	# 7 kingdoms
	'The_North', 'The_Stormlands', 'The_Westerlands', 'Dorne',
	'The_Reach', 'The_Vale_of_Arryn', 'The_Riverlands',
	
	# sub-regions in westeros
	'The_Crownlands', 'Iron_Islands',
	'Beyond_the_Wall', 'The_Fingers',
	'Bear_Island',

	# essos
	'Essos', 'Sothoryos', 'Summer_Isles',

	# ------
	# HOUSES
	# ------

	'House_Stark', 'House_Baratheon', 'House_Lannister', 'House_Targaryen',
	'House_Martell', 'House_Bolton', 'House_Tyrell', 'House_Mormont',
	'House_Baelish', 'House_Clegane', 'House_Tarly', 'House_Tarth',
	'House_Karstark', 'House_Umber', 'House_Tully', 'House_Frey',
	'Night\'s_Watch', 'House_Arryn', 'House_Greyjoy', 'House_Thorne',
	'House_Slynt',
	
	):
	# this_dict = {}
	if place != 'House_Stark' and skip:
		continue
	if place == 'The_North':
		pcount = 0
		print(']\n[')
		# print("\nRegions:\n")
		skip = False
		regions = True
		places = False
	if place == 'House_Stark':
		skip = False
		pcount = 0
		print(']\n[')
		# print("\nHouses:\n")
		houses = True
		regions = False
	if place == 'Winterfell':
		break
		skip = False
		pcount = 0
		print(']\n[')
		# print("\nPlaces:\n")
		people = False
		places = True
	print('\t{')
	pcount += 1
	#place = 'Winterfell'
	if people:
		print('\t\t\"model\": \"populate_content.person\", \"pk\": ' +  str(pcount) + ', \"fields\":\n\t\t{')
	site = 'http://gameofthrones.wikia.com/wiki/' + place
	page = urllib2.urlopen(site)
	soup = BeautifulSoup(page)
	# print(place + ':')
	if houses:
		print('\t\t\"model\": \"populate_content.house\", \"pk\": ' +  str(pcount) + ', \"fields\":\n\t\t{')
		hid = place.lower()
		print('\t\t\t\"house_id\": \"' + hid + '\",')
		hname = place.replace("_", " ")
		print('\t\t\t\"name\": \"' + hname + '\",')
	data = soup.find('div', id = "mw-content-text")
	if people:
		pid = place.replace("\'", "")
		pid = pid.lower()
		print('\t\t\t\"person_id\": \"' + pid + '\",')
		cut = place.find('_')
		if cut == -1:
			print('\t\t\t\"first_name\": ' + '\"' + place + '\",')
		else:
			print('\t\t\t\"first_name\": ' + '\"' + place[:cut] + '\",')
			print('\t\t\t\"last_name\": ' + '\"' + place[cut + 1:] + '\",')
		table = soup.find('table', attrs={'class': 'infobox'})
		for row in table.find_all('tr'):
			prnt = False
			status = False
			titles = False
			actor = False
			origin = False
			words = False
			for line in row.find_all('td'):
				text = str(line)
				if prnt:
					if titles:
						text = text.replace("</td>", "\"")
						text = text.replace("<br/>", ", ")
						
					while text.find('<') != -1 and text.find('>') != -1:
						start = text.find('<')
						cut = start
						end = text.find('>')

						while (start < end):
							start += 1
							if text[start] == '<':
								cut = start
						text = text[:cut] + text[end + 1:] #removed bracketed section
					if status:
						print('\t\t\t\"status\": ' + '\"' + text + '\",')
						# this_dict['status'] = text
						status = False
					if titles:
						# print('\t\t\t\t\t"' + text)
						# print('\t\t\t\t],')
						print('\t\t\t\"titles\": \"' + text + ',')
						titles = False
					if actor:
						print('\t\t\t\"actor\": \"' + text + '\",')
					# print(text)
				if text.find("Status") != -1:
					# print("Status:")
					status = True
					prnt = True
				if text.find("Origin") != -1:
					# print("Home:")
					origin = True
					prnt = True
				if text.find("Titles") != -1:
					# print('\t\t\t\"titles\":' + '\n\t\t\t\t[')
					titles = True
					prnt = True
				if text.find("Portrayed by") != -1:
					# print("Actor:")
					actor = True
					prnt = True
	else:
		table = soup.find('div', attrs={'style': "width:250px;float:right;clear:right;margin:1em 0 1em 1em;border:1px solid #000000;background:transparent;-moz-border-radius:10px;padding:10px 10px 10px 10px;"})
		if table != None:
			# print(table)
			location = False
			rulers = False
			prnt = False
			for row in table.find_all('div'):
				text = str(row)
				if places:
					if prnt:
						# if text.find("Location") != -1:
						# 	continue
						# if text.find("Rulers") != -1:
						# 	continue
						# if rulers:
						# 	text = text.replace("<br/>", "\n")
						while text.find('<') != -1 and text.find('>') != -1:
							start = text.find('<')
							cut = start
							end = text.find('>')
							while (start < end):
								start += 1
								if text[start] == '<':
									cut = start
							text = text[:cut] + text[end + 1:] #removed bracketed section
						# print(text)
						prnt = False
					# if text.find("Location") != -1:
					# 	print("Region:")
					# 	prnt = True
					# if text.find("Rulers") != -1:
					# 	print("Ruling Family:")
						# rulers = True
						# prnt = True
				if houses:
					if prnt:
						if text.find("Words") != -1:
							continue
						while text.find('<') != -1 and text.find('>') != -1:
							start = text.find('<')
							cut = start
							end = text.find('>')
							while (start < end):
								start += 1
								if text[start] == '<':
									cut = start
							text = text[:cut] + text[end + 1:] #removed bracketed section
						prnt = False
						if words:
							if text != '':
								text = text.replace('"','\\"')
								print('\t\t\t\"words\": \"' + text + '\",')
							words = False
					if text.find("Words") != -1:
						words = True
						prnt = True

	count = 0
	first = True
	for parag in data.find_all('p'):
		parag = str(parag)
		#Parse out any '<' or '>' and inbetween to remove ugly html
		while parag.find('<') != -1 and parag.find('>') != -1:
			start = parag.find('<')
			cut = start
			end = parag.find('>')

			while (start < end):
				start += 1
				if parag[start] == '<':
					cut = start
			parag = parag[:cut] + parag[end + 1:] #removed bracketed section
		#Parse out any brackets and references inbetween
		while parag.find('[') != -1 and parag.find(']') != -1:
			start = parag.find('[')
			cut = start
			end = parag.find(']')

			while (start < end):
				start += 1
				if parag[start] == '[':
					cut = start
			parag = parag[:cut] + parag[end + 1:] #removed bracketed section
		parag = parag.replace("\"", "\\\"") #add escape sequences
		#take out sentence long paragraphs or junk
		if parag.count(".") > 1:
			count += 1
			if count == 2 and not people and not houses:
				print("\nHistory:")
			if first:
				first = False
				print('\t\t\t\"description\": \"' + "<p>" + parag[:-1] + "</p>"),
			else:
				print("<p>" + parag[:-1] + "</p>"),
	print('\"')
	print('\t\t}')
	print('\t},')
print(']')