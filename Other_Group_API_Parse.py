from urllib.request import urlopen
import json

url = urlopen("http://gotopaws.me/api/pets/")
pets = json.loads(url.read().decode(url.info().get_param('charset') or 'utf-8'))

url = urlopen("http://gotopaws.me/api/shelters/")
shelters = json.loads(url.read().decode(url.info().get_param('charset') or 'utf-8'))

url = urlopen("http://gotopaws.me/api/cities/")
cities = json.loads(url.read().decode(url.info().get_param('charset') or 'utf-8'))

print(cities)