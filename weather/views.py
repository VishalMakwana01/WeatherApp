import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=52859687c521455b0ba8c720194b5b19"

    if request.method == 'POST':
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
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'temp_min': r['main']['temp_min'],
            'temp_max': r['main']['temp_max'],
            'humidity': r['main']['humidity']
        }
        weather_data.append(city_weather)

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weather/weather.html', context)
