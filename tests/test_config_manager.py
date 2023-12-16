import unittest
from unittest.mock import patch
from habittracker.config_manager import get_config_option, load_config


class TestConfigManager(unittest.TestCase):

    def setUp(self):
        # Setup a mock configuration for testing purposes
        self.mock_config = {
            'update_interval': 10,
            'tracked_apps': ['PyCharm', 'IntelliJ IDEA', 'Vim']
        }

    @patch('habittracker.config_manager.load_config')
    def test_get_config_option(self, mock_load_config):
        # Configure the mock to return the mock configuration
        mock_load_config.return_value = self.mock_config

        # Test for an integer option
        update_interval = get_config_option('update_interval')
        self.assertIsInstance(update_interval, int)
        self.assertEqual(update_interval, 10)

        # Test for a list option
        tracked_apps = get_config_option('tracked_apps')
        self.assertIsInstance(tracked_apps, list)
        self.assertEqual(tracked_apps, ['PyCharm', 'IntelliJ IDEA', 'Vim'])

        # Test for a missing option with a default
        missing_option = get_config_option('missing_option', 'default_value')
        self.assertIsInstance(missing_option, str)
        self.assertEqual(missing_option, 'default_value')


if __name__ == '__main__':
    unittest.main()
