import requests

city = "Moscow,RU"
appid = "********************************"

res = requests.get("https://api.openweathermap.org/data/2.5/forecast", params={'q': city, 'units': 'metric', 'lang': 'ru', 'appid': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print(f"Дата <{i['dt_txt']}> \r\n\
    Температура <{i['main']['temp']}> \r\n\
    Погодные условия <{i['weather'][0]['description']}> \r\n\
    Ветер <{i['wind']['speed']}> \r\n\
    Видимость <{i['visibility']}>")

    print("____________________________")
