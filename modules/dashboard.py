import requests, json, time, termux, logging

logging.basicConfig(
    filename='dashboard.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
    )

def run_dashboard():
    try:
        city = termux.API.location()[1]
        lat, lon = city['latitude'], city['longitude']
       
        city = requests.get(f'http://api.3geonames.org/{lat},{lon}.json', headers={'User-Agent': 'dashboardTermux'})
        city.raise_for_status()
       
        city_data = city.json()
        city = city_data['nearest']['city']

    except Exception as e:
        logging.error(f"Getting location from Termux API: {e}")
        config = json.load(open('config.json', 'r'))
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

    quote = requests.get('https://zenquotes.io/api/random', headers={'User-Agent': 'dashboardTermux'})
    quote.raise_for_status()

    quote_data = quote.json()[0]

    print(f"Dashboard for {city} - {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print('-' * 20)

    try:
        battery = termux.API.battery()[1]
        print(f"Battery level: {battery['level']}%")

    except Exception as e:
        logging.error(f"Getting battery status from Termux API: {e}")

    print(f"Temperature: {weather_info['temperature_2m']}°C")
    print(f"Humidity: {weather_info['relative_humidity_2m']}%")
    print(f"Is it day? {'Yes' if weather_info['is_day'] == 1 else 'No'}")
    print(f"Rain: {weather_info['rain']} mm")

    print('-' * 20)

    print("Quote of the day:")

    print(f"{quote_data['q']} - {quote_data['a']}")

if __name__ == "__main__":
    run_dashboard()