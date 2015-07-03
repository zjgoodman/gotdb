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
for name in ('Eddard_Stark', 'Tywin_Lannister', 'Robert_Baratheon'):
	# name = 'Eddard_Stark'
	site = 'http://www.westeros.org/GoT/Characters/Entry/' + name
	req = urllib2.Request(site, headers=hdr)
	page = urllib2.urlopen(req)
	soup = BeautifulSoup(page)
	print(name + ':')
	data = soup.find(id="Wrapper").find(id = "Main").find(id = "MainMiddle").find(id = "MainMiddleInner")
	for line in data.find('div', attrs={'class': 'CharActor'}):
		try:
			if line[1:].startswith("Played"):
				print(line[1:-1])
		except:
			pass
	# print(data.find('div', attrs={'class': 'CharActor'})[10:-4])
	for parag in data.find_all('p'):
		parag = str(parag)
		parag = parag.replace("<em>", "")
		parag = parag.replace("</em>", "")
		print(parag[3:-4])
	print('\n\n')

#using gameofthrones.wikia.com
#finds and scrapes info on all places and regions listed in string, places first
print("\nPlaces:\n")
regions = False
for place in ('Winterfell', 'Storm\'s_End', 'Casterly_Rock', 'The_North', 'The_Stormlands', 'The_Westerlands'):
	#place = 'Winterfell'
	if place == 'The_North':
		print("\nRegions:\n")
		regions = True
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
			parag = parag[:cut] + parag[end + 1:]
		#Parse out any brackets and references inbetween
		while parag.find('[') != -1 and parag.find(']') != -1:
			start = parag.find('[')
			cut = start
			end = parag.find(']')

			while (start < end):
				start += 1
				if parag[start] == '[':
					cut = start
			parag = parag[:cut] + parag[end + 1:]
		print(parag)
	print('\n\n')