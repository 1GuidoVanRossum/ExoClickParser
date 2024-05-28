from GetAllGroupIds import GetAllGroupIds
import requests
import pandas as pd


def GetCampaignsIds(token):
    idgroups = GetAllGroupIds(token)
    url = 'https://api.exoclick.com/v2/campaigns'
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    campaigns_info = []

    for id in idgroups:
        params = {
            'idgroup': id
        }
        response = requests.get(url, headers=headers, params=params)
        print(response)
        data = response.json()
        try:
            for campaign_id, campaign_details in data['result'].items():
                campaign_info = (campaign_details['id'], campaign_details['name'])
                campaigns_info.append(campaign_info)
        except AttributeError:
            pass

    return campaigns_info


def GetStatistics(all_campaign_ids, current_data, token):
    url = 'https://api.exoclick.com/v2/statistics/a/date'
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    stats = []
    for id in all_campaign_ids:
        params = {
            'campaignid': int(id[0]),
            'date-to': current_data,
            'date-from': current_data
        }
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        print(response)
        print(current_data)
        try:
            if data['result'] and (int(data['result'][0]['clicks']) != 0 or (int(data['result'][0]['impressions']) != 0 or int(data['result'][0]['video_hits']) != 0)):
                result = data['result'][0]
                stats.append({
                    'Date': result['ddate'],
                    'Campaign ID': id[0],
                    'Campaign Name': id[1],
                    'IMPRS': int(result['impressions']) + int(result['video_hits']),
                    'CLICKS': int(result['clicks']),
                    'Spend': float(result['cost']),
                })
                print(result)
        except KeyError:
            print(f'Error id: {id[0]}, data:{current_data}')

    return stats
