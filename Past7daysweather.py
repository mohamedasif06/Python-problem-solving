import requests
from datetime import datetime, timedelta
today = datetime.now()
week_ago = today - timedelta(days=7) #timedelta(days=) is used when you want to add or subtract a period of time from a date or time.
start_date = week_ago.strftime("%Y-%m-%d") #used to converting the date format (.strftime())
end_date = today.strftime("%Y-%m-%d")
url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
response = requests.get(url)
data = response.json()
print(data)
