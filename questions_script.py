import requests
import json

api_url = 'https://opentdb.com/api.php?amount=50&category=15&type=multiple'

response = requests.get(api_url)

if response.status_code == 200:
    new_data = response.json()
    with open('questionsdb.json', 'w') as json_file:
        json.dump(new_data, json_file, indent=2)
    print('Data saved to JSON file...')
else:
    print(f'Error: {response.status_code}')