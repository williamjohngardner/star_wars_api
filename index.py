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
        for item in response["results"]:
            index = item["url"].split('/')
            url_index = index[-2]
            print(url_index, item["name"])
        url = response['next']
        response = requests.get(url).json()
      else:
          for item in response["results"]:
              index = item["url"].split('/')
              url_index = index[-2]
              print(url_index, item["name"])
  new_choice = int(input("Enter ID Number To See Information on Person: "))
  url = "http://swapi.co/api/people"
  new_url = "{}/{}".format(url, new_choice)
  response = requests.get(new_url).json()
  for key, value in response.items():
      print(key, value)

if choice == 2:
  url = "http://swapi.co/api/films"
  response = requests.get(url).json()
  if response['next']:
      while response['next']:
          for item in response["results"]:
              index = item["url"].split('/')
              url_index = index[-2]
              print(url_index, item["title"])
          url = response['next']
          response = requests.get(url).json()
      else:
          false
  for item in response["results"]:
      index = item["url"].split('/')
      url_index = index[-2]
      print(url_index, item["title"])
  new_choice = int(input("Enter ID Number To See Information on the Film: "))
  url = "http://swapi.co/api/films"
  new_url = "{}/{}".format(url, new_choice)
  response = requests.get(new_url).json()
  for key, value in response.items():
      print(key, value)

if choice == 3:
  url = "http://swapi.co/api/vehicles"
  response = requests.get(url).json()
  if response['next']:
      while response['next']:
          for item in response["results"]:
              index = item["url"].split('/')
              url_index = index[-2]
              print(url_index, index["name"])
          url = response['next']
          response = requests.get(url).json()
      else:
          for item in response["results"]:
              index = item["url"].split('/')
              url_index = index[-2]
              print(url_index, item["name"])
  new_choice = int(input("Enter ID Number To See Information on Vehicle: "))
  url = "http://swapi.co/api/vehicles"
  new_url = "{}/{}".format(url, new_choice)
  response = requests.get(new_url).json()
  for key, value in response.items():
      print(key, value)
