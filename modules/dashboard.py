import requests, json, time

def run_dashboard():
    config  = json.load(open('config.json', 'r'))
    city = config['city']

    location = requests.get(
        'https://nominatim.openstreetmap.org/search', 
        params={'q': city, 'format': 'json', 'limit': 1},
        headers={'User-Agent': 'dashboardTermux'}
        )

    location.raise_for_status()

    loc_data = location.json()
    if not loc_data:
        raise ValueError(f"City '{city}' not found in Nominatim database.")
        
    lat, lon = loc_data[0]['lat'], loc_data[0]['lon']
    time.sleep(1)

    weather = requests.get(f'https://api.open-meteo.com/v1/forecast', params={
        'latitude': lat,
        'longitude': lon,
        'current': 'temperature_2m,relative_humidity_2m,is_day,rain',
        'timezone': 'America/Sao_Paulo'
    }, headers={'User-Agent': 'dashboardTermux'})

    weather.raise_for_status()

    weather_data = weather.json()
    weather_info = weather_data['current']

    print(f"Current weather in {city}:")
    print(f"Temperature: {weather_info['temperature_2m']}°C")
    print(f"Humidity: {weather_info['relative_humidity_2m']}%")
    print(f"Is it day? {'Yes' if weather_info['is_day'] == 1 else 'No'}")
    print(f"Rain: {weather_info['rain']} mm")

if __name__ == "__main__":
    run_dashboard()