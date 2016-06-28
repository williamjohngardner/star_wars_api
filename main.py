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
  url_index = ""
  response = requests.get(url).json()
  if response['next']:
      while response['next']:
        for person in response["results"]:
            index = person["url"].split('/')
            url_index = index[-2]
            print(person["url"])
            print(person["name"])
        url = response['next']
        response = requests.get(url).json()
      else:
          for person in response["results"]:
              index = person["url"].split('/')
              url_index = index[-2]
              print(person["url"])
              print(person["name"])
  new_choice = int(input("Enter Number: "))
  #print(url/{}.format(url_index)


if choice == 2:
  url = "http://swapi.co/api/films"
  response = requests.get(url).json()
  if response['next']:
      while response['next']:
          for film in response["results"]:
              print(film["title"])
          url = response['next']
          response = requests.get(url).json()
      else:
          false
  for film in response["results"]:
      print(film["title"])

if choice == 3:
  url = "http://swapi.co/api/vehicles"
  response = requests.get(url).json()
  if response['next']:
      while response['next']:
          for vehicle in response["results"]:
              print(vehicle["name"])
          url = response['next']
          response = requests.get(url).json()
      else:
          for vehicle in response["results"]:
              print(vehicle["name"])
