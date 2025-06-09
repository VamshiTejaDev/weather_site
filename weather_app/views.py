from django.shortcuts import render
import requests
from django.conf import settings

def weather_view(request):
    weather_data = {}
    city = ""

    if request.method == 'POST':
        city = request.POST.get('city')
        url = f"http://api.weatherapi.com/v1/current.json?key={settings.WEATHER_API_KEY}&q={city}&aqi=no"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': city,
                'temperature': data['current']['temp_c'],
                'description': data['current']['condition']['text'],
                'humidity': data['current']['humidity'],
                'wind': data['current']['wind_kph'],
                'icon': data['current']['condition']['icon']
            }
        else:
            weather_data = {'error': 'City not found'}

    return render(request, 'weather_app/weather.html', {'weather': weather_data, 'city': city})