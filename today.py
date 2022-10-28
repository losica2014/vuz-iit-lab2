import requests

city = "Moscow,RU"
appid = "********************************"

res = requests.get("https://api.openweathermap.org/data/2.5/weather", params={'q': city, 'units': 'metric', 'lang': 'ru', 'appid': appid})
data = res.json()

print("Город:", city)
print("Температура:", data["main"]["temp"])
print("Погодные условия:", data['weather'][0]['description'])
print("Ветер:", data['wind']['speed'])
print("Видимость:", data['visibility'])
