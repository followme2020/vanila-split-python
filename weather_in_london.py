import json
import requests

response = requests.get("https://samples.openweathermap.org/data/2.5/weather?q=Orlando&appid=b6907d289e10d714a6e88b30761fae22")
data = response.json()

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
print(data)

items = json.loads(response.text)
print(items)
gps = items['coord']
print(items['coord'])
print(type(gps))
for i in gps:
    print(i, ' ', gps[i])

print(items['weather'])
weater = items['weather']
print(weater[0]['description'])

print(items['main'])
tempk = items['main']
kelvin = tempk['temp']
celsius = kelvin - 273.15
print(celsius)

print(items['wind'])

print(items['clouds'])

print(items['name'])


