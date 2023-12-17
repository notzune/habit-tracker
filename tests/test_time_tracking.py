import unittest
from unittest.mock import patch
from habittracker.time_tracking import start_timer, stop_timer, get_time_spent, time_spent, last_app_name, last_start_time


class TestTimeTracking(unittest.TestCase):

    def setUp(self):
        # Reset global variables before each test
        time_spent.clear()
        global last_app_name, last_start_time
        last_app_name = None
        last_start_time = None

    @patch('your_module.time.time', side_effect=[100, 105])
    def test_time_tracking(self, mock_time):
        # Simulate starting and stopping the timer
        start_timer("ExampleApp")
        stop_timer()

        # Check if time spent is recorded correctly
        self.assertEqual(time_spent, {"ExampleApp": 5})

        # Check if the last app name and last start time are reset
        self.assertIsNone(last_app_name)
        self.assertIsNone(last_start_time)

    @patch('your_module.time.time', side_effect=[100, 110, 115])
    def test_multiple_apps(self, mock_time):
        # Simulate switching between apps
        start_timer("ExampleApp")
        start_timer("AnotherApp")
        stop_timer()

        # Check if time spent is recorded correctly
        self.assertEqual(time_spent, {"ExampleApp": 10, "AnotherApp": 5})


if __name__ == '__main__':
    unittest.main()
