import requests

def get_token():
    url = 'https://api.exoclick.com/v2/login'

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    data = {
        "username": "",
        "password": "",
        "api_token": ""
    }

    response = requests.post(url, headers=headers, json=data)
    data = response.json()
    return data['token']
