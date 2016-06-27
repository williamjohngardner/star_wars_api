import requests


choice = int(input('''
    ***STAR WARS SWAPI DATABASE***
    Enter a Number to Explore SWAPI
    1 - List of Characters
    2 - List of Films
    3 - List of Vehicles
'''))

if choice == 1:
  url = "http://swapi.co/api/people"
  response = requests.get(url).json()
  for person in response["results"]:
      print(person["name"])

if choice == 2:
  url = "http://swapi.co/api/films"
  response = requests.get(url).json()
  for film in response["results"]:
      print(film["title"])

if choice == 3:
  url = "http://swapi.co/api/vehicles"
  response = requests.get(url).json()
  for vehicle in response["results"]:
      print(vehicle["name"])
