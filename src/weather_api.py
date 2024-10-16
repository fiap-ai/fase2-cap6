import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"
GEO_URL = "http://api.openweathermap.org/geo/1.0/direct"

def get_coordinates(city_name, country_code):
    params = {
        "q": f"{city_name},{country_code}",
        "limit": 1,
        "appid": API_KEY
    }
    response = requests.get(GEO_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['lat'], data[0]['lon']
    return None, None

def fetch_weather_data(city_name, country_code, units='metric', lang='en'):
    if not API_KEY:
        print("Erro: Chave da API OpenWeatherMap não encontrada. Verifique o arquivo .env.")
        return None

    lat, lon = get_coordinates(city_name, country_code)
    if lat is None or lon is None:
        print(f"Erro: Não foi possível encontrar coordenadas para {city_name}, {country_code}")
        return None

    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": units,
        "lang": lang
    }

    current_response = requests.get(WEATHER_URL, params=params)
    forecast_response = requests.get(FORECAST_URL, params=params)
    
    if current_response.status_code == 200 and forecast_response.status_code == 200:
        current_data = current_response.json()
        forecast_data = forecast_response.json()
        processed_data = process_weather_data(current_data, forecast_data)
        
        print("Debug - Dados processados em fetch_weather_data:")
        for day in processed_data['daily']:
            print(f"Data: {day['date']}, Precipitação: {day['precipitation']:.2f} mm")
        
        return processed_data
    else:
        print(f"Erro ao buscar dados: {current_response.status_code}, {forecast_response.status_code}")
        print(f"Mensagem de erro: {current_response.text}, {forecast_response.text}")
        return None

def process_weather_data(current_data, forecast_data):
    processed_data = {
        "current": current_data,
        "hourly": forecast_data['list'],
        "daily": []
    }

    daily_data = {}
    for forecast in forecast_data['list']:
        date = datetime.fromtimestamp(forecast['dt']).strftime('%Y-%m-%d')
        rain = forecast.get('rain', {}).get('3h', 0)
        snow = forecast.get('snow', {}).get('3h', 0)
        precipitation = rain + snow
        
        if date not in daily_data:
            daily_data[date] = {
                'date': date,
                'temperature': forecast['main']['temp'],
                'temp_min': forecast['main']['temp_min'],
                'temp_max': forecast['main']['temp_max'],
                'weather': forecast['weather'][0],
                'precipitation': precipitation
            }
        else:
            daily_data[date]['temp_min'] = min(daily_data[date]['temp_min'], forecast['main']['temp_min'])
            daily_data[date]['temp_max'] = max(daily_data[date]['temp_max'], forecast['main']['temp_max'])
            daily_data[date]['precipitation'] += precipitation

    processed_data['daily'] = list(daily_data.values())
    processed_data['daily'].sort(key=lambda x: x['date'])

    print("Debug - Dados processados:")
    for day in processed_data['daily']:
        print(f"Data: {day['date']}, Temp: {day['temperature']:.2f}°C, Min: {day['temp_min']:.2f}°C, Max: {day['temp_max']:.2f}°C, Precipitação: {day['precipitation']:.2f} mm")

    return processed_data

if __name__ == "__main__":
    city_name = "Rio de Janeiro"
    country_code = "BR"
    data = fetch_weather_data(city_name, country_code)
    if data:
        print(f"Dados atuais para {city_name}:")
        print(f"Temperatura: {data['current']['main']['temp']}°C")
        print(f"Descrição: {data['current']['weather'][0]['description']}")
        print(f"\nPrevisão para os próximos {len(data['daily'])} dias (limitado pela API gratuita):")
        for day in data['daily']:
            print(f"{day['date']}: Max {day['temp']['max']}°C, Min {day['temp']['min']}°C, Precipitação: {day['precipitation']:.1f}mm, {day['weather'][0]['description']}")
