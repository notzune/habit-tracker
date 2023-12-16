from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import os
import pickle

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def get_user_timezone(service):
    calendar_list = service.calendarList().list().execute()
    user_timezone = calendar_list['items'][0]['timeZone']
    return user_timezone


def get_calendar_service():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service


def create_or_update_event(service, time_data):
    # Assuming time_data is a dictionary with 'start_time' and 'end_time' as datetime objects
    user_timezone = get_user_timezone(service)

    event = {
        'summary': 'Programming Time',
        'description': 'Time spent on programming.',
        'start': {
            'dateTime': time_data['start_time'].isoformat(),
            'timeZone': user_timezone,
        },
        'end': {
            'dateTime': time_data['end_time'].isoformat(),
            'timeZone': user_timezone,
        },
    }

    # Call the Calendar API to create an event
    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f"Event created: {event.get('htmlLink')}")


# Example usage
if __name__ == "__main__":
    service = get_calendar_service()
    # Call create_or_update_event with appropriate data
