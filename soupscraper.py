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
for name in ('Eddard_Stark', 'Tywin_Lannister', 'Robert_Baratheon'):
	# name = 'Eddard_Stark'
	site = 'http://www.westeros.org/GoT/Characters/Entry/' + name
	hdr = {'User-Agent': 'Mozilla/5.0'}
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
	print('\n')