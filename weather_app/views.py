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




def weather_map(request):
    if request.method == 'POST':
        city_name = request.POST.get('city_name')

        if city_name:
            # Create the URL for the Weatherbit.io API request
            base_url = 'https://maps.weatherbit.io/v2.0/satellite/vis/now/2/0/0.png'
            api_key = '2d096ccf7b4c462ea8047a30ffec8b89'
            url = f'{base_url}?key={api_key}&city={city_name}'

            # Make a request to Weatherbit.io to get the satellite map
            response = requests.get(url)
            print(url)

            if response.status_code == 200:
                # Render an HTML template with the map image
                context = {'map_image_url': response.url}
                return render(request, 'weather_app/weather_map_error.html', context)

    # If no city name is provided or an error occurs, display a form
    return render(request, 'weather_app/weather_map.html')