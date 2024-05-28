import requests

def get_token():
    url = 'https://api.exoclick.com/v2/login'

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    data = {
        "username": "Fora23",
        "password": "4BOr%40B0r%40",
        "api_token": "78c873edb46d4be1ca6f79cc6b20552deed41a13"
    }

    response = requests.post(url, headers=headers, json=data)
    data = response.json()
    return data['token']