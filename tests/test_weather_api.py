import unittest
import sys
import os
from unittest.mock import patch, Mock

# Adiciona o diretório 'src' ao PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from weather_api import fetch_weather_data, get_coordinates

class TestWeatherAPI(unittest.TestCase):
    @patch('src.weather_api.requests.get')
    def test_fetch_weather_data_success(self, mock_get):
        # Mock para get_coordinates
        mock_get.side_effect = [
            Mock(status_code=200, json=lambda: [{'lat': -22.9068, 'lon': -43.1729}]),
            Mock(status_code=200, json=lambda: {
                'main': {'temp': 25},
                'weather': [{'description': 'clear sky'}]
            }),
            Mock(status_code=200, json=lambda: {
                'list': [
                    {
                        'dt': 1625097600,
                        'main': {'temp': 26, 'temp_min': 24, 'temp_max': 28},
                        'weather': [{'description': 'sunny'}],
                        'rain': {'3h': 0}
                    }
                ]
            })
        ]

        city_name = "Rio de Janeiro"
        country_code = "BR"
        data = fetch_weather_data(city_name, country_code)
        
        self.assertIsNotNone(data)
        self.assertIn('current', data)
        self.assertIn('daily', data)
        self.assertEqual(data['current']['main']['temp'], 25)
        self.assertEqual(data['daily'][0]['temp_max'], 28)
        self.assertEqual(data['daily'][0]['temp_min'], 24)
        self.assertEqual(data['daily'][0]['precipitation'], 0)

    @patch('src.weather_api.requests.get')
    def test_fetch_weather_data_invalid_city(self, mock_get):
        mock_get.return_value = Mock(status_code=404, json=lambda: [])
        data = fetch_weather_data("Invalid City", "US")
        self.assertIsNone(data)

    @patch('src.weather_api.requests.get')
    def test_fetch_weather_data_invalid_country(self, mock_get):
        mock_get.return_value = Mock(status_code=404, json=lambda: [])
        data = fetch_weather_data("New York", "XX")
        self.assertIsNone(data)

    @patch('src.weather_api.requests.get')
    def test_get_coordinates(self, mock_get):
        mock_get.return_value = Mock(status_code=200, json=lambda: [{'lat': -22.9068, 'lon': -43.1729}])
        lat, lon = get_coordinates("Rio de Janeiro", "BR")
        self.assertAlmostEqual(lat, -22.9068, places=4)
        self.assertAlmostEqual(lon, -43.1729, places=4)

    @patch('src.weather_api.requests.get')
    def test_fetch_weather_data_units(self, mock_get):
        # Mock para get_coordinates e fetch_weather_data
        mock_get.side_effect = [
            Mock(status_code=200, json=lambda: [{'lat': -22.9068, 'lon': -43.1729}]),
            Mock(status_code=200, json=lambda: {
                'main': {'temp': 25},
                'weather': [{'description': 'clear sky'}]
            }),
            Mock(status_code=200, json=lambda: {'list': []}),
            Mock(status_code=200, json=lambda: [{'lat': -22.9068, 'lon': -43.1729}]),
            Mock(status_code=200, json=lambda: {
                'main': {'temp': 77},  # 25°C converted to Fahrenheit
                'weather': [{'description': 'clear sky'}]
            }),
            Mock(status_code=200, json=lambda: {'list': []})
        ]

        data_metric = fetch_weather_data("Rio de Janeiro", "BR", units='metric')
        self.assertEqual(data_metric['current']['main']['temp'], 25)  # Celsius

        data_imperial = fetch_weather_data("Rio de Janeiro", "BR", units='imperial')
        self.assertEqual(data_imperial['current']['main']['temp'], 77)  # Fahrenheit

if __name__ == '__main__':
    unittest.main()
