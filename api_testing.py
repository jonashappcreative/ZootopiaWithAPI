import json
import requests
API_KEY = "wbvM4JFhbZZA1fhJnftgdv6F59dpO1sFkqBkvn9d"

name = input("Please ask for an animal: ")

api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
if response.status_code == requests.codes.ok:
    print(response.json())
else:
    print("Error:", response.status_code, response.text)