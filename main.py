from ExtractInfo import GetCampaignsIds, GetStatistics
from CreateTable import CreateTable
from datetime import datetime, timedelta
from api_request import get_token
print("Введите дату YYYY-MM-DD")
data = input()
start_date = datetime.strptime(data, "%Y-%m-%d")
print("Подождите, идёт загрузка!")

token = get_token()
print(token)
all_campaign_ids = GetCampaignsIds(token)
print(all_campaign_ids)
for i in range(7):
    current_date = start_date + timedelta(days=i)
    stats = GetStatistics(all_campaign_ids, current_date.strftime("%Y-%m-%d"), token)
    print(f'Создаю {i+1} таблицу!')
    CreateTable(stats, i+1)

