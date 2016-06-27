import requests

url = "http://swapi.co/api/people"

response = requests.get(url).json()

for person in response["results"]:
    print(person["name"])
