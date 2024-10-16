import unittest
import sys
import os
from unittest.mock import patch, Mock

# Adiciona o diretório 'src' ao PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from climate_data import ClimateData
from climate_analysis import generate_report, plot_climate_data
from weather_api import fetch_weather_data, get_coordinates
from database import create_table, insert_data, fetch_data

class IntegrationTest(unittest.TestCase):
    def setUp(self):
        self.climate_data = ClimateData()
        self.test_location = "Test City"
        create_table()  # Ensure the database table exists

    @patch('weather_api.get_coordinates')
    @patch('weather_api.requests.get')
    def test_data_flow(self, mock_requests_get, mock_get_coordinates):
        # Mock the coordinates
        mock_get_coordinates.return_value = (40.7128, -74.0060)  # New York coordinates

        # Mock the API responses
        mock_current_response = Mock()
        mock_current_response.status_code = 200
        mock_current_response.json.return_value = {'main': {'temp': 25}, 'weather': [{'description': 'clear sky'}]}

        mock_forecast_response = Mock()
        mock_forecast_response.status_code = 200
        mock_forecast_response.json.return_value = {
            'list': [
                {
                    'dt': 1625097600,
                    'main': {'temp': 26, 'temp_min': 24, 'temp_max': 28},
                    'weather': [{'description': 'sunny'}],
                    'rain': {'3h': 10}
                },
                {
                    'dt': 1625184000,
                    'main': {'temp': 27, 'temp_min': 25, 'temp_max': 29},
                    'weather': [{'description': 'partly cloudy'}],
                    'rain': {'3h': 5}
                },
                {
                    'dt': 1625270400,
                    'main': {'temp': 26, 'temp_min': 24, 'temp_max': 28},
                    'weather': [{'description': 'light rain'}],
                    'rain': {'3h': 15}
                }
            ]
        }

        mock_requests_get.side_effect = [mock_current_response, mock_forecast_response]

        # Fetch data from weather API
        api_data = fetch_weather_data(self.test_location, "BR")
        print(f"API Data: {api_data}")  # Debug print
        self.assertIsNotNone(api_data)

        # Insert data into the database
        for day in api_data['daily']:
            insert_data(self.test_location, day['date'], day['temperature'], day['precipitation'])

        # Fetch data from the database
        db_data = fetch_data(self.test_location)
        print(f"DB Data: {db_data}")  # Debug print
        self.assertIsNotNone(db_data)
        self.assertTrue(len(db_data) > 0)

        # Generate report
        report = generate_report(self.test_location, db_data, temp_threshold=30, precip_threshold=50)
        self.assertIsNotNone(report)
        self.assertIn(self.test_location, report)

        # Plot climate data
        plot_file = plot_climate_data(self.test_location, db_data)
        self.assertIsNotNone(plot_file)
        self.assertTrue(os.path.exists(plot_file))

    def test_analysis_integration(self):
        # Add sample data
        sample_data = [
            {'date': '2023-01-01', 'temperature': 25, 'precipitation': 10},
            {'date': '2023-01-02', 'temperature': 30, 'precipitation': 5},
            {'date': '2023-01-03', 'temperature': 28, 'precipitation': 15},
        ]
        for data in sample_data:
            self.climate_data.add_data(self.test_location, data['temperature'], data['precipitation'], data['date'])

        # Fetch data and generate report
        data = self.climate_data.get_data(self.test_location)
        report = generate_report(self.test_location, data, temp_threshold=28, precip_threshold=12)

        # Check if report contains expected information
        self.assertIn("Alerta de alta temperatura", report)
        self.assertIn("Alerta de alta precipitação", report)

    def tearDown(self):
        # Clean up any created data or files
        self.climate_data.clear_data()
        # Remove any created plot files
        if os.path.exists('build'):
            for file in os.listdir('build'):
                if file.endswith('.png'):
                    os.remove(os.path.join('build', file))

if __name__ == '__main__':
    unittest.main()
