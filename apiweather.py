import requests
def get_weather(city,api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    print(data["main"])
api_key = "1dcc96b8c9ff91598dc9ffa972461546"
get_weather("bangalore",api_key)

