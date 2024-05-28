from datetime import datetime, timedelta

# Задаем начальную дату в формате ГГГГ-ММ-ДД
start_date_str = "2024-04-01"  # Пример начальной даты
start_date = datetime.strptime(start_date_str, "%Y-%m-%d")

# Проходим по циклу в течение 7 дней
for i in range(7):
    current_date = start_date + timedelta(days=i)