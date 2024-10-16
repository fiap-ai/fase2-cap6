import os
import sys
import unittest
from datetime import datetime, timedelta

# Adiciona o diretório 'src' ao PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from climate_data import ClimateData

class TestOracleCRUD(unittest.TestCase):
    def setUp(self):
        self.climate_data = ClimateData()
        self.location = "Test City"
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.time = "12:00:00 PM"
        self.temperature = 25.5
        self.precipitation = 10.2

    def test_oracle_crud(self):
        # Criar um item
        print("1. Criando um novo item:")
        self.climate_data.add_data(self.location, self.temperature, self.precipitation, self.date, self.time)
        
        # Mostrar o item
        print("\n2. Mostrando o item criado:")
        data = self.climate_data.get_data(self.location)
        print(data)
        self.assertIsNotNone(data)
        self.assertTrue(len(data) > 0)
        
        # Atualizar o item
        new_temperature = 26.0
        new_precipitation = 15.5
        print("\n3. Atualizando o item:")
        self.climate_data.update_data(self.location, self.date, self.time, new_temperature, new_precipitation)
        
        # Mostrar o item atualizado
        print("\n4. Mostrando o item atualizado:")
        updated_data = self.climate_data.get_data(self.location)
        print(updated_data)
        self.assertIsNotNone(updated_data)
        self.assertEqual(updated_data[0]['temperature'], new_temperature)
        self.assertEqual(updated_data[0]['precipitation'], new_precipitation)
        
        # Remover o item
        print("\n5. Removendo o item:")
        self.climate_data.delete_data(self.location, self.date, self.time)
        
        # Tentar mostrar o item removido
        print("\n6. Tentando mostrar o item removido:")
        removed_data = self.climate_data.get_data(self.location)
        print(removed_data)
        self.assertEqual(len(removed_data), 0)

    def tearDown(self):
        # Limpar dados após cada teste
        self.climate_data.clear_data()

if __name__ == "__main__":
    unittest.main()
