import unittest
import sys
import os
import time
from datetime import datetime, timedelta

# Adiciona o diretório 'src' ao PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from climate_data import ClimateData
from climate_analysis import generate_report
from database import create_table, insert_data_batch, fetch_data, get_unique_locations, delete_all_data

class PerformanceTest(unittest.TestCase):
    def setUp(self):
        self.climate_data = ClimateData()
        create_table()
        self.test_location = "Performance Test City"
        self.large_dataset = self.generate_large_dataset()
        delete_all_data()  # Ensure the database is empty before each test

    def generate_large_dataset(self):
        start_date = datetime(2020, 1, 1)
        dataset = []
        for i in range(1000):  # Generate 1000 days of data
            date = start_date + timedelta(days=i)
            dataset.append((
                self.test_location,
                date,
                20 + (i % 20),  # Temperature between 20 and 39
                i % 100  # Precipitation between 0 and 99
            ))
        return dataset

    def test_database_insert_performance(self):
        start_time = time.time()
        batch_size = 100  # Insert 100 records at a time
        for i in range(0, len(self.large_dataset), batch_size):
            batch = self.large_dataset[i:i+batch_size]
            insert_data_batch(batch)
        end_time = time.time()
        
        execution_time = end_time - start_time
        self.assertLess(execution_time, 30)  # Assuming insertion should take less than 30 seconds
        print(f"Time taken to insert 1000 records: {execution_time:.2f} seconds")

    def test_database_fetch_performance(self):
        # First, insert the data
        insert_data_batch(self.large_dataset)

        start_time = time.time()
        fetched_data = fetch_data(self.test_location)
        end_time = time.time()

        execution_time = end_time - start_time
        self.assertLess(execution_time, 5)  # Assuming fetch should take less than 5 seconds
        self.assertEqual(len(fetched_data), 1000)  # Ensure all data was fetched
        print(f"Time taken to fetch 1000 records: {execution_time:.2f} seconds")

    def tearDown(self):
        # Clean up the database after tests
        delete_all_data()

if __name__ == '__main__':
    unittest.main()
