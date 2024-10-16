import os
import sys
import unittest
from datetime import datetime

# Adiciona o diretório 'src' ao PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from database import create_table, insert_data, fetch_data, get_unique_locations, delete_all_data

class TestOracleDatabase(unittest.TestCase):
    def setUp(self):
        create_table()

    def tearDown(self):
        delete_all_data()

    def test_database_operations(self):
        print("Testing database operations:")
        
        # Inserir dados
        test_date = datetime.now()
        insert_data("Test City", test_date, 25.5, 10.2)
        
        # Buscar dados
        data = fetch_data("Test City")
        print(f"Fetched data: {data}")
        self.assertIsNotNone(data)
        self.assertTrue(len(data) > 0)
        
        # Verificar localizações únicas
        locations = get_unique_locations()
        print(f"Unique locations: {locations}")
        self.assertIn("Test City", locations)
        
        print("All database tests completed.")

if __name__ == "__main__":
    unittest.main()
