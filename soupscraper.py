import urllib2
from bs4 import BeautifulSoup

testpage = urllib2.urlopen('http://gameofthrones.wikia.com/wiki/House_Stark')
soup = BeautifulSoup(testpage.read())
for link in soup.find_all('a'):
	print(link.get('title'))