"""post_request.py

    Author: Bruno Cayres Messias <bruno.messias@strattner.com.br>
    Date: 07/13/2021

    Revision: [DATE/NAME]
    - 

Description:
Library tha contain the codes to implement connection to the API defined
"""
import requests
import json


def search_data(API_URL):
    """search_data Get the response from the server tha was sended

    :param API_URL: API Url of the server to get data from
    :type API_URL: String
    """
    request = requests.get(API_URL)
    data = json.loads(request.content)
    print(data)


def send_data(API_URL, JSON_PATH):
    """send_data Send data from json file to an specific API

    :param API_URL: The API URL
    :type API_URL: String
    :param JSON_PATH: The path to the json file tha contain data to send
    :type JSON_PATH: String
    """
    with open(JSON_PATH) as json_file:
        json_data = json.load(json_file)

    requests.post(API_URL, json=json_data)
