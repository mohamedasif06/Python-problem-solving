import requests
from datetime import datetime, timedelta
import pandas as pd

today = datetime.now()
week_ago = today - timedelta(days=7)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
response = requests.get(url)
data = response.json()
print(data)

daily_data = data["daily"]

df = pd.DataFrame({
    'date': daily_data["time"],
    'max_temp':daily_data["temperature_2m_max"],
    'min_temp':daily_data["temperature_2m_min"]
})

df['date'] = pd.to_datetime(df["date"])
print(df)
