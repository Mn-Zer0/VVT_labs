import requests as r
import json


# city_name = str(input('Город: '))
city_name = 'Москва'
API_key = 'aa79cdf019e8bc51e35c611243e0ecf8'

s1 = r.get("http://api.openweathermap.org/data/2.5/forecast", params={'q': city_name, 'units': 'metric', 'lang': 'ru',
                                                                      'APPID': API_key})
m1 = s1.json()

print('Прогноз на день:')
for i in m1['list']:
    print(i['dt_txt'], i['wind']['speed'], i['visibility'])
    print('-' * 30)


s2 = r.get("http://api.openweathermap.org/data/2.5/weather", params={'q': city_name, 'units': 'metric', 'lang': 'ru',
                                                                     'APPID': API_key})
m2 = s1.json()

print('Прогноз на неделю:')
for i in m2['list']:
    print(i['dt_txt'], i['wind']['speed'], i['visibility'])
    print('-' * 30)
