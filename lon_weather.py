# -*- coding: utf-8 -*-


import json
import requests

response_london = requests.get("http://dataservice.accuweather.com/currentconditions/v1/328328?apikey=CVuuyJGd5ur53RrE6csG3KTDXmt3PpwM&language=en&details=true")
london = response_london.json()

lontext = london[0]['WeatherText']
# print(type(lontext))
print('The weather in London right now is ' + lontext)
lonprectype = london[0]['PrecipitationType']
lonprecip = london[0]['HasPrecipitation']
# print(type(lonprecip))
print("Any precipitation ")
if lonprecip == True:
    print('Yes')
    print(lonprectype)
else:
    print("No")
londaytime = london[0]['IsDayTime']
# print(type(londaytime))
print('What time of day?')
if londaytime:
    print("Day time")
else:
    print("Night")
lontemp = london[0]['Temperature']['Metric']['Value']
# print(type(lontemp))
print('The temperature is ', lontemp, ' celsius')
lonrealf = london[0]['RealFeelTemperature']['Metric']['Value']
# print(type(lonrealf))
print('It feels like ', lonrealf, 'celsius')
lonhumidity = london[0]['RelativeHumidity']
# print(type(lonhumidity))
print('Humidity ', lonhumidity, '%')
lonwinddirection = london[0]['Wind']['Direction']
# print(type(lonwinddirection))
print('Wind direction is ', lonwinddirection['English'], lonwinddirection['Degrees'])
lonwindspeed = london[0]['Wind']['Speed']['Metric']['Value']
# print(type(lonwindspeed))
print('Wind speed is ', lonwindspeed, 'km/h')
lonuvitext = london[0]['UVIndexText']
# print(type(lonuvitext))
print('UV index: ' + lonuvitext)
lonpressure = london[0]['Pressure']['Metric']['Value']
# print(type(lonpressure))
print('Atmospheric pressure: ', lonpressure/1000, 'Atm')
print(london)
# response_berlin = requests.get("http://dataservice.accuweather.com/currentconditions/v1/178087?apikey=CVuuyJGd5ur53RrE6csG3KTDXmt3PpwM&language=en&details=true")
# berlin = response_berlin.json()
# print(berlin)

# 249758 amsterdam
# 215819 tel aviv