# views.py
from django.shortcuts import render
import requests

def index(request):
    return render(request,'weather_app/index.html')

def get_weather_data(city_name):
    # Replace 'YOUR_API_KEY' with your OpenWeatherMap API key.
    api_key = '160464886eb090fe3ced0490a1d50ebd'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    response = requests.get(base_url)
    data = response.json()
    return data

def weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        weather_data = get_weather_data(city)
        return render(request, 'weather_app/weather.html', {'weather_data': weather_data})
    else:
        return render(request, 'weather_app/weather.html')


def weather_forecast(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = '160464886eb090fe3ced0490a1d50ebd'
        base_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
        response = requests.get(base_url)
        data = response.json()
        forecasts = data.get('list', [])

        return render(request, 'weather_app/weather_forecast.html', {'forecasts': forecasts, 'city': city})
    else:
        return render(request, 'weather_app/weather_forecast.html')
