import json
import requests

response_jerusalem = requests.get("http://dataservice.accuweather.com/currentconditions/v1/213225?apikey=CVuuyJGd5ur53RrE6csG3KTDXmt3PpwM&language=en&details=true")
jerusalem = response_jerusalem.json()

jertext = jerusalem[0]['WeatherText']
# print(type(jertext))
print('The weather in Jerusalem right now is ' + jertext)
jerprecip = jerusalem[0]['HasPrecipitation']
# print(type(jerprecip))
# print("Any precipitation " + jerprecip)
jerprectype = jerusalem[0]['PrecipitationType']
# print(type(jerprectype))
# print('Precipitation type ' + jerprectype)
jerdaytime = jerusalem[0]['IsDayTime']
# print(type(jerdaytime))
# print('Is it day time?' + jerdaytime)
jertemp = jerusalem[0]['Temperature']['Metric']['Value']
# print(type(jertemp))
print('The temperature is ', jertemp, ' celsius')
jerrealf = jerusalem[0]['RealFeelTemperature']['Metric']['Value']
# print(type(jerrealf))
print('It feels like ', jerrealf, 'celsius')
jerhumidity = jerusalem[0]['RelativeHumidity']
# print(type(jerhumidity))
print('Humidity ', jerhumidity, '%')
jerwinddirection = jerusalem[0]['Wind']['Direction']
# print(type(jerwinddirection))
print('Wind direction is ', jerwinddirection['English'], jerwinddirection['Degrees'])
jerwindspeed = jerusalem[0]['Wind']['Speed']['Metric']['Value']
# print(type(jerwindspeed))
print('Wind speed is ', jerwindspeed, 'km/h')
jeruvitext = jerusalem[0]['UVIndexText']
# print(type(jeruvitext))
print('UV index: ' + jeruvitext)
jerpressure = jerusalem[0]['Pressure']['Metric']['Value']
# print(type(jerpressure))
print('Atmospheric pressure: ', jerpressure/1000, 'Atm')
print(jerusalem)

