import json
import requests

response = requests.get("http://dataservice.accuweather.com/currentconditions/v1/topcities/150?apikey=CVuuyJGd5ur53RrE6csG3KTDXmt3PpwM&language=en")
data = response.json()

print(type(data))
print(data)


cities = json.loads(response.text)
print(cities)
print(type(cities))


with open("cities_file.json", "w") as write_file:
    json.dump(data, write_file)
print(data)

with open("cities_file.json", "r") as read_ff:
    d = json.load(read_ff)
    for item in d:
        print(type(item))

    print(d)
