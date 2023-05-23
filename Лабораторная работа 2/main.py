import requests as r
import json


# city_name = str(input('Город: '))
city_name = 'Москва'
API_key = 'aa79cdf019e8bc51e35c611243e0ecf8'

s1 = r.get("http://api.openweathermap.org/data/2.5/forecast", params={'q': city_name, 'units': 'metric', 'lang': 'ru',
                                                                      'APPID': API_key})
m1 = s1.json()

print('Прогноз на неделю:')
for i in m1['list']:
    print('Дата:', i['dt_txt'] )
    print('Скорость ветра:', i['wind']['speed'])
    print('Видимость:', i['visibility'])
    print('-' * 30)


s2 = r.get("http://api.openweathermap.org/data/2.5/weather", params={'q': city_name, 'units': 'metric', 'lang': 'ru',
                                                                     'APPID': API_key})
m2 = s2.json()
print('-' * 30)
print("TEST")
print(s2.text)
print(m2)
print('-' * 30)
print('Прогноз на день:')
print('Скорость ветра:', m2['wind']['speed'])
print('Видимость:', m2['visibility'])
print('-' * 30)
