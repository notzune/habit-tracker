import yaml
import os

config_file_path = 'config.yaml'

# Default configuration
default_config = {
    'tracked_apps': ['PyCharm', 'IntelliJ IDEA', 'Vim'],
    'update_interval': 10,  # Time in seconds
}


def load_config():
    # Load the configuration file into a dictionary
    if not os.path.exists(config_file_path):
        # If the configuration file doesn't exist, create it with the default config
        save_config(default_config)
        return default_config
    else:
        with open(config_file_path, 'r') as config_file:
            return yaml.safe_load(config_file) or default_config


def save_config(config):
    # Save the given configuration dictionary to the configuration file
    with open(config_file_path, 'w') as config_file:
        yaml.dump(config, config_file, default_flow_style=False)


def get_config_option(key):
    # Get a specific configuration option by key
    config = load_config()
    return config.get(key)


def set_config_option(key, value):
    # Set a specific configuration option
    config = load_config()
    config[key] = value
    save_config(config)


# Example usage
if __name__ == "__main__":
    current_config = load_config()
    print(f"Current configuration: {current_config}")
    print(f"Tracked applications: {get_config_option('tracked_apps')}")
    set_config_option('tracked_apps', ['PyCharm', 'Vim'])
    print(f"Updated tracked applications: {get_config_option('tracked_apps')}")
