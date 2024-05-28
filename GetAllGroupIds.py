import requests


def GetAllGroupIds(token):
    url = 'https://api.exoclick.com/v2/campaigns/groups'

    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    response = requests.get(url, headers=headers)
    print(response)
    data = response.json()

    idgroups = [group['idgroup'] for group in data['result']]

    return idgroups
