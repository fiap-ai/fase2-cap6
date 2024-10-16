import unittest
import sys
import os
from datetime import datetime, timedelta

# Adiciona o diretório 'src' ao PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from climate_data import ClimateData

class ClimateDataTest(unittest.TestCase):
    def setUp(self):
        self.climate_data = ClimateData()
        self.test_location = "Test City"
        self.test_date = datetime.now().strftime("%Y-%m-%d")
        self.test_time = "12:00:00 PM"
        self.test_temperature = 25.5
        self.test_precipitation = 10.2

    def test_add_and_get_data(self):
        self.climate_data.add_data(self.test_location, self.test_temperature, self.test_precipitation, self.test_date, self.test_time)
        data = self.climate_data.get_data(self.test_location)
        self.assertIsNotNone(data)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['temperature'], self.test_temperature)
        self.assertEqual(data[0]['precipitation'], self.test_precipitation)

    def test_update_data(self):
        self.climate_data.add_data(self.test_location, self.test_temperature, self.test_precipitation, self.test_date, self.test_time)
        new_temperature = 26.0
        new_precipitation = 15.5
        self.climate_data.update_data(self.test_location, self.test_date, self.test_time, new_temperature, new_precipitation)
        data = self.climate_data.get_data(self.test_location)
        self.assertEqual(data[0]['temperature'], new_temperature)
        self.assertEqual(data[0]['precipitation'], new_precipitation)

    def test_delete_data(self):
        self.climate_data.add_data(self.test_location, self.test_temperature, self.test_precipitation, self.test_date, self.test_time)
        self.climate_data.delete_data(self.test_location, self.test_date, self.test_time)
        data = self.climate_data.get_data(self.test_location)
        self.assertEqual(len(data), 0)

    def test_get_data_with_date_range(self):
        start_date = datetime.now() - timedelta(days=5)
        end_date = datetime.now()
        for i in range(10):
            date = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
            self.climate_data.add_data(self.test_location, self.test_temperature, self.test_precipitation, date, self.test_time)
        
        filtered_data = self.climate_data.get_data(self.test_location, start_date.date(), end_date.date())
        self.assertEqual(len(filtered_data), 6)  # 5 days + today

    def test_get_all_locations(self):
        locations = ["City A", "City B", "City C"]
        for location in locations:
            self.climate_data.add_data(location, self.test_temperature, self.test_precipitation, self.test_date, self.test_time)
        
        all_locations = self.climate_data.get_all_locations()
        self.assertEqual(set(all_locations), set(locations))

    def test_get_data_nonexistent_location(self):
        data = self.climate_data.get_data("Nonexistent City")
        self.assertEqual(len(data), 0)

    def test_update_nonexistent_data(self):
        self.climate_data.update_data("Nonexistent City", self.test_date, self.test_time, 30.0, 20.0)
        data = self.climate_data.get_data("Nonexistent City")
        self.assertEqual(len(data), 0)

    def test_get_data_ordered_by_date(self):
        dates = ["2023-01-03", "2023-01-01", "2023-01-02"]
        for date in dates:
            self.climate_data.add_data(self.test_location, self.test_temperature, self.test_precipitation, date, self.test_time)
        
        data = self.climate_data.get_data(self.test_location)
        self.assertEqual(len(data), 3)
        self.assertEqual(data[0]['date'], "2023-01-01")
        self.assertEqual(data[1]['date'], "2023-01-02")
        self.assertEqual(data[2]['date'], "2023-01-03")

    def test_add_invalid_data(self):
        with self.assertRaises(ValueError):
            self.climate_data.add_data(self.test_location, "invalid", self.test_precipitation, self.test_date, self.test_time)
        
        with self.assertRaises(ValueError):
            self.climate_data.add_data(self.test_location, self.test_temperature, "invalid", self.test_date, self.test_time)

    def tearDown(self):
        self.climate_data.clear_data()

if __name__ == '__main__':
    unittest.main()
