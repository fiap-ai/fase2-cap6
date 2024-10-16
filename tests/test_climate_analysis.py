import unittest
import sys
import os
import math

# Adiciona o diretório 'src' ao PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from climate_analysis import calculate_spi, generate_alerts, generate_recommendations

class ClimateAnalysisTest(unittest.TestCase):
    def setUp(self):
        self.sample_data = [
            {'date': '2023-01-01', 'precipitation': 10},
            {'date': '2023-01-02', 'precipitation': 20},
            {'date': '2023-01-03', 'precipitation': 30},
            {'date': '2023-01-04', 'precipitation': 15},
            {'date': '2023-01-05', 'precipitation': 25},
        ]

    def test_calculate_spi(self):
        spi = calculate_spi(self.sample_data)
        self.assertIsInstance(spi, float)
        self.assertTrue(math.isfinite(spi))  # Verifica se o SPI é um número finito

    def test_calculate_spi_known_data(self):
        known_data = [
            {'date': '2023-01-01', 'precipitation': 10},
            {'date': '2023-01-02', 'precipitation': 20},
            {'date': '2023-01-03', 'precipitation': 30},
        ]
        calculated_spi = calculate_spi(known_data)
        self.assertIsInstance(calculated_spi, float)
        self.assertTrue(math.isfinite(calculated_spi))

    def test_generate_alerts(self):
        data = [
            {'date': '2023-01-01', 'temperature': 35, 'precipitation': 60},
            {'date': '2023-01-02', 'temperature': 28, 'precipitation': 40},
            {'date': '2023-01-03', 'temperature': 32, 'precipitation': 55},
        ]
        alerts = generate_alerts(data, temp_threshold=30, precip_threshold=50)
        self.assertIsInstance(alerts, list)
        expected_alerts = [
            "Alerta de alta temperatura em 2023-01-01 12:00:00 AM: 35.0°C",
            "Alerta de alta precipitação em 2023-01-01 12:00:00 AM: 60.0mm",
            "Alerta de alta temperatura em 2023-01-03 12:00:00 AM: 32.0°C",
            "Alerta de alta precipitação em 2023-01-03 12:00:00 AM: 55.0mm"
        ]
        self.assertEqual(set(alerts), set(expected_alerts))
        self.assertEqual(len(alerts), 4)  # 2 temperatura alta (35, 32) e 2 precipitação alta (60, 55)

    def test_generate_alerts_different_thresholds(self):
        data = [
            {'date': '2023-01-01', 'temperature': 35, 'precipitation': 60},
            {'date': '2023-01-02', 'temperature': 28, 'precipitation': 40},
            {'date': '2023-01-03', 'temperature': 32, 'precipitation': 55},
        ]
        alerts_high = generate_alerts(data, temp_threshold=40, precip_threshold=70)
        self.assertEqual(len(alerts_high), 0)  # No alerts should be generated

        alerts_low = generate_alerts(data, temp_threshold=25, precip_threshold=30)
        self.assertEqual(len(alerts_low), 6)  # All data points should generate alerts

    def test_generate_recommendations(self):
        alerts = [
            "Alerta de alta temperatura em 2023-01-01: 35.0°C",
            "Alerta de alta precipitação em 2023-01-01: 60.0mm",
        ]
        recommendations = generate_recommendations(alerts)
        self.assertIsInstance(recommendations, list)
        self.assertTrue(any("temperatura" in rec.lower() for rec in recommendations))
        self.assertTrue(any("precipitação" in rec.lower() for rec in recommendations))

    def test_generate_recommendations_specific_alerts(self):
        temp_alerts = ["Alerta de alta temperatura em 2023-01-01: 35.0°C"]
        temp_recommendations = generate_recommendations(temp_alerts)
        self.assertTrue(any("temperatura" in rec.lower() for rec in temp_recommendations))
        self.assertFalse(any("precipitação" in rec.lower() for rec in temp_recommendations))

        precip_alerts = ["Alerta de alta precipitação em 2023-01-01: 60.0mm"]
        precip_recommendations = generate_recommendations(precip_alerts)
        self.assertTrue(any("precipitação" in rec.lower() for rec in precip_recommendations))
        self.assertFalse(any("temperatura" in rec.lower() for rec in precip_recommendations))

if __name__ == '__main__':
    unittest.main()
