import unittest
from habittracker.app_detection import get_active_window_title


class TestAppDetection(unittest.TestCase):

    def test_get_active_window_title(self):
        # Mock the OS-specific functionality, if necessary
        title = get_active_window_title()
        # Assert that the title is a string (or whatever is expected)
        self.assertIsInstance(title, str)


if __name__ == '__main__':
    unittest.main()
