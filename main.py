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
  if response['next']:
      while response['next']:
        for person in response["results"]:
            index = person["url"].split('/')
            print(index[-2])
            print(person["name"])
            # print(person["url"])
        url = response['next']
        response = requests.get(url).json()
      else:
          for person in response["results"]:
              index = person["url"].split('/')
              print(index[-2])
              print(person["name"])
  new_choice = int(input("Enter Number: "))
# from here i need to find a way to take the index variable above and append it
# to the url to show the API data for the aforementioned page.

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
