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
people = True
places = False
regions = False
houses = False
pcount = 0
main_dict = []
print('[')
for place in ('Eddard_Stark', 'Tywin_Lannister', 'Robert_Baratheon', 'Daenerys_Targaryen', 'Jon_Snow', 'Sansa_Stark', 'Arya_Stark', 'Stannis_Baratheon', 'Tyrion_Lannister', 'Theon_Greyjoy', 'Joffrey_Baratheon', 'Ramsay_Bolton', 'Cersei_Lannister', 'Bran_Stark', 'Margaery_Tyrell', 'Melisandre', 'Daario_Naharis', 'Jaime_Lannister', 'Robb_Stark', 'Jorah_Mormont', 'Petyr_Baelish', 'Tommen_Baratheon', 'Sandor_Clegane', 'Jaqen_H\'ghar', 'Gendry', 'Drogo', 'Brienne_of_Tarth', 'Ygritte', 'Roose_Bolton', 'Catelyn_Stark', 'Varys', 'Bronn', 'Viserys_Targaryen', 'Shae', 'Talisa_Stark', 'Ellaria_Sand', 'Jeor_Mormont', 'Samwell_Tarly', 'Davos_Seaworth', 'Gilly', 'Tormund', 'Missandei', 'Grey_Worm', 'Winterfell', 'Storm\'s_End', 'Casterly_Rock', 'Dragonstone', 'Pyke_(castle)', 'The_Dreadfort', 'King\'s_Landing', 'Highgarden', 'Asshai', 'Tyrosh', 'Bear_Island', 'The_Fingers', 'Clegane\'s_Keep', 'Braavos', 'Vaes_Dothrak', 'Evenfall_Hall', 'Riverrun', 'Lys', 'Lorath', 'Volantis', 'Hellholt', 'Horn_Hill', 'Craster\'s_Keep', 'Summer_Isles', 'Naath', 'The_North', 'The_Stormlands', 'The_Westerlands', 'Iron_Islands', 'The_Crownlands', 'The_Reach', 'Essos', 'Sothoryos', 'The_Vale_of_Arryn', 'Beyond_the_Wall', 'The_Riverlands', 'Dorne', 'House_Stark', 'House_Baratheon', 'House_Lannister', 'House_Targaryen', 'House_Martell', 'House_Bolton', 'House_Tyrell', 'House_Mormont', 'House_Baelish', 'House_Clegane', 'House_Tarly'):
	this_dict = {}
	if place == 'The_North':
		count = 0
		print(']\n[')
		# print("\nRegions:\n")
		regions = True
		places = False
	if place == 'House_Stark':
		count = 0
		print(']\n[')
		# print("\nHouses:\n")
		houses = True
		regions = False
	if place == 'Winterfell':
		break
		count = 0
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
	data = soup.find('div', id = "mw-content-text")
	if people:
		pid = place.replace("\'", "")
		pid = pid.lower()
		print('\t\t\t\"person_id\": "' + pid + '\",')
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
						this_dict['status'] = text
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
						if text.find("Location") != -1:
							continue
						if text.find("Rulers") != -1:
							continue
						if rulers:
							text = text.replace("<br/>", "\n")
						while text.find('<') != -1 and text.find('>') != -1:
							start = text.find('<')
							cut = start
							end = text.find('>')
							while (start < end):
								start += 1
								if text[start] == '<':
									cut = start
							text = text[:cut] + text[end + 1:] #removed bracketed section
						print(text)
						prnt = False
					if text.find("Location") != -1:
						print("Region:")
						prnt = True
					if text.find("Rulers") != -1:
						print("Ruling Family:")
						rulers = True
						prnt = True
				# if regions:

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
			if count == 2 and not people:
				print("\nHistory:")
			if first:
				first = False
				print('\t\t\t\"bio\": \"' + "<p>" + parag[:-1] + "</p>"),
			else:
				print("<p>" + parag[:-1] + "</p>"),
	print('\"')
	print('\t\t}')
	print('\t},')
print(']')
print('\n\n')
main_dict += this_dict

print(main_dict)