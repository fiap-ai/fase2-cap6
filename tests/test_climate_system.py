import os
import sys
import shutil
import unittest
import random
from datetime import datetime, timedelta

# Adiciona o diretório 'src' ao PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from climate_data import ClimateData
from climate_analysis import (
    generate_report, plot_climate_data, export_to_csv,
    compare_cities, generate_comparison_report, plot_moving_average
)

class TestClimateSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.clear_build_folder()

    @staticmethod
    def clear_build_folder():
        build_path = os.path.join(os.path.dirname(__file__), '..', 'build')
        if os.path.exists(build_path):
            shutil.rmtree(build_path)
        os.makedirs(build_path)
        print("Build folder cleared and recreated.")

    @staticmethod
    def generate_sample_data(location, days=30):
        climate_data = ClimateData()
        start_date = datetime.now() - timedelta(days=days)
        
        data = []
        for i in range(days):
            date = start_date + timedelta(days=i)
            temperature = random.uniform(20, 35)
            precipitation = random.uniform(0, 100)
            data.append({
                'date': date.strftime("%Y-%m-%d"),
                'temperature': temperature,
                'precipitation': precipitation
            })
        
        return data

    def test_climate_system(self):
        print("Testing Climate Monitoring and Risk Management System")
        
        # Gerar dados de amostra para Rio de Janeiro e Goiás
        rio_data = self.generate_sample_data("Rio de Janeiro")
        goias_data = self.generate_sample_data("Goiás")
        
        # Testar geração de relatório
        report = generate_report("Rio de Janeiro", rio_data, temp_threshold=30, precip_threshold=50)
        self.assertIsNotNone(report)
        print("\nGenerated Report for Rio de Janeiro:")
        print(report)
        
        # Testar plotagem de dados climáticos
        plot_climate_data("Rio de Janeiro", rio_data)
        self.assertTrue(os.path.exists(os.path.join('build', 'Rio de Janeiro_climate_data.png')))
        print("\nClimate data plot generated for Rio de Janeiro.")
        
        # Testar exportação para CSV
        export_to_csv("Rio de Janeiro", rio_data, "rio_climate_data.csv")
        self.assertTrue(os.path.exists(os.path.join('build', 'rio_climate_data.csv')))
        print("\nClimate data exported to CSV for Rio de Janeiro.")
        
        # Testar comparação de cidades
        cities_data = {"Rio de Janeiro": rio_data, "Goiás": goias_data}
        compare_cities(cities_data)
        self.assertTrue(os.path.exists(os.path.join('build', 'cities_comparison.png')))
        comparison_report = generate_comparison_report(cities_data, temp_threshold=30, precip_threshold=50)
        self.assertIsNotNone(comparison_report)
        print("\nCities Comparison Report:")
        print(comparison_report)
        
        # Testar média móvel
        plot_moving_average("Rio de Janeiro", rio_data, window=7)
        self.assertTrue(os.path.exists(os.path.join('build', 'Rio de Janeiro_moving_average.png')))
        print("\nMoving average plot generated for Rio de Janeiro.")
        
        print("\nAll tests completed successfully.")

if __name__ == "__main__":
    unittest.main()
