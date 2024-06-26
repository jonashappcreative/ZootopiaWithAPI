import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


def fetch_data(user_request):
    """
    Fetches the animals data for the animal 'user_request'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {
        ...
      },
      'locations': [
        ...
      ],
      'characteristics': {
        ...
      }
    },
    """
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(user_request)
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        # print(response.json())
        return response.json()
    else:
        print("Error:", response.status_code, response.text)


# data = fetch_data(user_request)
# print(data)
