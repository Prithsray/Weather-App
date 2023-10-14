# views.py
from django.shortcuts import render
import requests


def index(request):
    # Access user-specific session data (e.g., user's first name)
    user_first_name = request.session.get('user_id','user_first_name')
    
    # Render the template and pass the session data in the context
    return render(request, 'weather_app/index.html', {'user_first_name': user_first_name})

def get_weather_data(city_name):
    # Replace 'YOUR_API_KEY' with your OpenWeatherMap API key.
    api_key = '160464886eb090fe3ced0490a1d50ebd'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    response = requests.get(base_url)
    data = response.json()
    return data

def weather(request):
    user_first_name = request.session.get('user_id','user_first_name')

    if request.method == 'POST':
        city = request.POST.get('city')
        weather_data = get_weather_data(city)
        return render(request, 'weather_app/weather.html', {'weather_data': weather_data})
    else:
        return render(request, 'weather_app/weather.html',{'user_first_name': user_first_name})


def weather_forecast(request):
    user_first_name = request.session.get('user_id','user_first_name')

    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = '160464886eb090fe3ced0490a1d50ebd'
        base_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
        response = requests.get(base_url)
        data = response.json()
        forecasts = data.get('list', [])

        return render(request, 'weather_app/weather_forecast.html', {'forecasts': forecasts, 'city': city})
    else:
        return render(request, 'weather_app/weather_forecast.html',{'user_first_name': user_first_name})
