import json
import os

CONFIG_FILE = 'build/config.json'
DEFAULT_TEMP_THRESHOLD = 30
DEFAULT_PRECIP_THRESHOLD = 50

def load_config():
    os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        config = {}

    # Use environment variables if available, otherwise use saved config or defaults
    config['temp_threshold'] = float(os.getenv('TEMP_THRESHOLD', config.get('temp_threshold', DEFAULT_TEMP_THRESHOLD)))
    config['precip_threshold'] = float(os.getenv('PRECIP_THRESHOLD', config.get('precip_threshold', DEFAULT_PRECIP_THRESHOLD)))

    return config

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

def reset_to_defaults():
    config = {
        'temp_threshold': DEFAULT_TEMP_THRESHOLD,
        'precip_threshold': DEFAULT_PRECIP_THRESHOLD
    }
    save_config(config)
    return config

# Initialize config file with default values if it doesn't exist
if not os.path.exists(CONFIG_FILE):
    reset_to_defaults()
