import requests 
import json

def search_data(API_URL):
    request = requests.get(API_URL)
    data = json.loads(request.content)
    print(data)

def send_data(API_URL, JSON_PATH):
    with open(JSON_PATH) as json_file:
        json_data = json.load(json_file)

    requests.post(API_URL, json=json_data)
  