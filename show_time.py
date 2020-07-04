from flask import Flask, render_template, request, redirect, url_for
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


cities_key_api = {'London': 'http://dataservice.accuweather.com/currentconditions/v1/328328?apikey=CVuuyJGd5ur53RrE6csG3KTDXmt3PpwM&language=en&details=true',
                  'Jerusalem': 'http://dataservice.accuweather.com/currentconditions/v1/213225?apikey=CVuuyJGd5ur53RrE6csG3KTDXmt3PpwM&language=en&details=true',
                  'Berlin': 'http://dataservice.accuweather.com/currentconditions/v1/178087?apikey=CVuuyJGd5ur53RrE6csG3KTDXmt3PpwM&language=en&details=true',
                  'Tel aviv': 'http://dataservice.accuweather.com/currentconditions/v1/215819?apikey=CVuuyJGd5ur53RrE6csG3KTDXmt3PpwM&language=en&details=true',
                  'Amsterdam': 'http://dataservice.accuweather.com/currentconditions/v1/249758?apikey=CVuuyJGd5ur53RrE6csG3KTDXmt3PpwM&language=en&details=true'}


@app.route('/')
def index():
    cities = cities_key_api
    return render_template('index.html', cities=cities)


@app.route('/weather/<string:name>')
def weather(name):
    key = cities_key_api[name]
    temp_data_set = requests.get(key)
    complete_info = temp_data_set.json()
    weathertext = complete_info[0]['WeatherText']
    preciptype = complete_info[0]['PrecipitationType']
    temperature = complete_info[0]['Temperature']['Metric']['Value']
    realf = complete_info[0]['RealFeelTemperature']['Metric']['Value']
    humidity = complete_info[0]['RelativeHumidity']
    winddirection = complete_info[0]['Wind']['Direction']
    windspeed = complete_info[0]['Wind']['Speed']['Metric']['Value']
    uvitext = complete_info[0]['UVIndexText']
    pressure = complete_info[0]['Pressure']['Metric']['Value']
    return render_template('show_weather.html', weathertext=weathertext, preciptype=preciptype, temperature=temperature,
                           realf=realf, humidity=humidity, winddirection=winddirection, windspeed=windspeed,
                           uvitext=uvitext, pressure=pressure, name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)