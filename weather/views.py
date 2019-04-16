import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=52859687c521455b0ba8c720194b5b19"

    if request.method == 'POST':
        if '_add' in request.POST:
            form = CityForm(request.POST)
            form.save()

    form = CityForm()
    cities = City.objects.all()
    weather_data = []
    for city in cities:

        r = requests.get(url.format(city)).json()
        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'icon': r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weather/weather.html', context)


def details(request):

    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=52859687c521455b0ba8c720194b5b19"
    url1 = "http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid=c2e1ee8338f97ec7253d06766ad6d8aa"
    cities = City.objects.all()
    weather_data = []
    weather_forecast = []
    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'temp_min': r['main']['temp_min'],
            'temp_max': r['main']['temp_max'],
            'humidity': r['main']['humidity'],
            'main': r['weather'][0]['main'],
            'speed': r['wind']['speed']
        }
        weather_data.append(city_weather)
        s = requests.get(url1.format(city)).json()

        city_forecast = {
            'city': city.name,
            'date0': s['list'][0]['dt_txt'],
            'temp0': s['list'][0]['main']['temp'],
            'description0': s['list'][0]['weather'][0]['description'],
            'humidity0': s['list'][0]['main']['humidity'],
            'icon0': s['list'][0]['weather'][0]['icon'],
            'date1': s['list'][1]['dt_txt'],
            'temp1': s['list'][1]['main']['temp'],
            'description1': s['list'][1]['weather'][0]['description'],
            'humidity1': s['list'][1]['main']['humidity'],
            'icon1': s['list'][1]['weather'][0]['icon'],
            'date2': s['list'][2]['dt_txt'],
            'temp2': s['list'][2]['main']['temp'],
            'description2': s['list'][2]['weather'][0]['description'],
            'humidity2': s['list'][2]['main']['humidity'],
            'icon2': s['list'][2]['weather'][0]['icon'],
            'date3': s['list'][3]['dt_txt'],
            'temp3': s['list'][3]['main']['temp'],
            'description3': s['list'][3]['weather'][0]['description'],
            'humidity3': s['list'][3]['main']['humidity'],
            'icon3': s['list'][3]['weather'][0]['icon'],
            'date4': s['list'][4]['dt_txt'],
            'temp4': s['list'][4]['main']['temp'],
            'description4': s['list'][4]['weather'][0]['description'],
            'humidity4': s['list'][4]['main']['humidity'],
            'icon4': s['list'][4]['weather'][0]['icon'],
            'date5': s['list'][5]['dt_txt'],
            'temp5': s['list'][5]['main']['temp'],
            'description5': s['list'][5]['weather'][0]['description'],
            'humidity5': s['list'][5]['main']['humidity'],
            'icon5': s['list'][5]['weather'][0]['icon'],


        }
        weather_forecast.append(city_forecast)
    print(weather_forecast)
    context = {'weather_data': weather_data,
               'weather_forecast': weather_forecast}

    return render(request, 'weather/details.html', context)
