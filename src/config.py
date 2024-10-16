import json
import os

CONFIG_FILE = 'build/config.json'

def load_config():
    os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
    try:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            'temp_threshold': 30,
            'precip_threshold': 50
        }

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)

def get_thresholds():
    config = load_config()
    return config['temp_threshold'], config['precip_threshold']

def set_thresholds(temp_threshold, precip_threshold):
    config = load_config()
    config['temp_threshold'] = temp_threshold
    config['precip_threshold'] = precip_threshold
    save_config(config)
