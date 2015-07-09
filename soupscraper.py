import urllib2
from bs4 import BeautifulSoup

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
print("People:\n")
for name in ('Eddard_Stark', 'Tywin_Lannister', 'Robert_Baratheon', 'Daenerys_Targaryen', 'Jon_Snow', 'Sansa_Stark', 'Arya_Stark', 'Stannis_Baratheon', 'Tyrion_Lannister', 'Theon_Grejoy', 'Joffrey_Baratheon', 'Ramsay_Bolton', 'Cersei_Lannister', 'Bran_Stark', 'Margaery_Tyrell', 'Melisandre_of_Asshai', 'Daario_Naharis', 'Jaime_Lannister', 'Robb_Stark', 'Jorah_Mormont', 'Petyr_Baelish', 'Tommen_Baratheon', 'Sandor_Clegane', 'Jaqen_Hghar', 'Gendry', 'Khal_Drogo', 'Brienne_of_Tarth', 'Ygritte', 'Roose_Bolton', 'Catelyn_Stark', 'Varys', 'Bronn', 'Viserys_Targaryen', 'Shae', 'Talisa_Stark', 'Ellaria_Sand', 'Jeor_Mormont', 'Samwell_Tarly', 'Davos_Seaworth', 'Gilly', 'Tormund', 'Missandei'):
	# name = 'Eddard_Stark'
	site = 'http://www.westeros.org/GoT/Characters/Entry/' + name
	req = urllib2.Request(site, headers=hdr)
	page = urllib2.urlopen(req)
	soup = BeautifulSoup(page)
	print(name + ':')
	data = soup.find(id="Wrapper").find(id = "Main").find(id = "MainMiddle").find(id = "MainMiddleInner")
	for line in data.find('div', attrs={'class': 'CharActor'}):
		try:
			if line[1:].startswith("Played"): #find line with actor name
				print(line[1:-1])
		except:
			pass
	# print(data.find('div', attrs={'class': 'CharActor'})[10:-4])
	for parag in data.find_all('p'):
		parag = str(parag)
		parag = parag.replace("<em>", "")
		parag = parag.replace("</em>", "")
		print(parag[3:-4]) #removes html brackets
	print('\n\n')

#using gameofthrones.wikia.com
#finds and scrapes info on all places and regions listed in string, places first
print("\nPlaces:\n")
regions = False
houses = False
for place in ('Winterfell', 'Storm\'s_End', 'Casterly_Rock', 'Dragonstone', 'Pyke_(castle)', 'The_Dreadfort', 'King\'s_Landing', 'Highgarden', 'Asshai', 'Tyrosh', 'Bear_Island', 'The_Fingers', 'Clegane\'s_Keep', 'Braavos', 'Vaes_Dothrak', 'Evenfall_Hall', 'Riverrun', 'Lys', 'Lorath', 'Volantis', 'Hellholt', 'Horn_Hill', 'Craster\'s_Keep', 'The_North', 'The_Stormlands', 'The_Westerlands', 'Iron_Islands', 'The_Crownlands', 'The_Reach', 'Essos', 'The_Vale_of_Arryn', 'Beyond_the_Wall', 'The_Riverlands', 'Dorne', 'House_Stark', 'House_Baratheon', 'House_Lannister', 'House_Targaryen', 'House_Martell', 'House_Bolton', 'House_Tyrell', 'House_Mormont', 'House_Baelish', 'House_Clegane'):
	#place = 'Winterfell'
	if place == 'The_North':
		print("\nRegions:\n")
		regions = True
	if place == 'House_Stark':
		print("\nHouses:\n")
		houses = True
	site = 'http://gameofthrones.wikia.com/wiki/' + place
	page = urllib2.urlopen(site)
	soup = BeautifulSoup(page)
	print(place + ':')
	data = soup.find('div', id = "mw-content-text")
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
		#take out sentence long paragraphs or junk
		if parag.count(".") > 1:
			print("<p>" + parag + "</p>")
	print('\n\n')