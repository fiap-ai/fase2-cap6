import unittest
import os
import sys
import json

# Adiciona o diretório 'src' ao PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from config import load_config, get_thresholds, set_thresholds, reset_to_defaults, CONFIG_FILE, DEFAULT_TEMP_THRESHOLD, DEFAULT_PRECIP_THRESHOLD

class ConfigTest(unittest.TestCase):
    def setUp(self):
        # Salvar o conteúdo original do arquivo de configuração, se existir
        self.original_config = None
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                self.original_config = f.read()

        # Resetar para os valores padrão no início de cada teste
        reset_to_defaults()

    def tearDown(self):
        # Restaurar o conteúdo original do arquivo de configuração, se existia
        if self.original_config is not None:
            with open(CONFIG_FILE, 'w') as f:
                f.write(self.original_config)
        elif os.path.exists(CONFIG_FILE):
            os.remove(CONFIG_FILE)

        # Limpar variáveis de ambiente após os testes
        if 'TEMP_THRESHOLD' in os.environ:
            del os.environ['TEMP_THRESHOLD']
        if 'PRECIP_THRESHOLD' in os.environ:
            del os.environ['PRECIP_THRESHOLD']

    def test_load_config(self):
        config = load_config()
        self.assertIn('temp_threshold', config)
        self.assertIn('precip_threshold', config)
        self.assertEqual(config['temp_threshold'], DEFAULT_TEMP_THRESHOLD)
        self.assertEqual(config['precip_threshold'], DEFAULT_PRECIP_THRESHOLD)

    def test_get_thresholds(self):
        temp_threshold, precip_threshold = get_thresholds()
        self.assertEqual(temp_threshold, DEFAULT_TEMP_THRESHOLD)
        self.assertEqual(precip_threshold, DEFAULT_PRECIP_THRESHOLD)

    def test_set_thresholds(self):
        set_thresholds(40, 150)
        temp_threshold, precip_threshold = get_thresholds()
        self.assertEqual(temp_threshold, 40)
        self.assertEqual(precip_threshold, 150)

    def test_reset_to_defaults(self):
        set_thresholds(40, 150)
        reset_to_defaults()
        config = load_config()
        self.assertEqual(config['temp_threshold'], DEFAULT_TEMP_THRESHOLD)
        self.assertEqual(config['precip_threshold'], DEFAULT_PRECIP_THRESHOLD)

    def test_environment_variables_priority(self):
        os.environ['TEMP_THRESHOLD'] = '35'
        os.environ['PRECIP_THRESHOLD'] = '100'
        config = load_config()
        self.assertEqual(config['temp_threshold'], 35)
        self.assertEqual(config['precip_threshold'], 100)

    def test_default_values(self):
        # Ensure no environment variables are set
        if 'TEMP_THRESHOLD' in os.environ:
            del os.environ['TEMP_THRESHOLD']
        if 'PRECIP_THRESHOLD' in os.environ:
            del os.environ['PRECIP_THRESHOLD']

        # Remove the config file to test default values
        if os.path.exists(CONFIG_FILE):
            os.remove(CONFIG_FILE)

        config = load_config()
        self.assertEqual(config['temp_threshold'], DEFAULT_TEMP_THRESHOLD)
        self.assertEqual(config['precip_threshold'], DEFAULT_PRECIP_THRESHOLD)

if __name__ == '__main__':
    unittest.main()
