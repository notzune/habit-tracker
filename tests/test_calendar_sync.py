from unittest.mock import patch, Mock
import unittest
from habittracker.calendar_sync import create_or_update_event

# Sample data for the test
your_test_event_data = {
    'start_time': '2021-01-01T09:00:00Z',
    'end_time': '2021-01-01T10:00:00Z',
    'summary': 'Test Event',
    'description': 'Testing event creation'
}


class TestCalendarSync(unittest.TestCase):

    @patch('habittracker.calendar_sync.get_calendar_service')
    def test_create_or_update_event(self, mock_service):
        # Mock the Google Calendar API service object
        mock_service.return_value.events.return_value.insert.return_value.execute.return_value = {
            'id': '12345',
            'htmlLink': 'https://calendar.google.com/event?id=12345'
        }

        # Call the function using the mock
        service = mock_service.return_value
        result = create_or_update_event(service, your_test_event_data)

        # Assert that the service's insert method was called with the correct parameters
        service.events.return_value.insert.assert_called_once()
        # Assert that the result is not None
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
